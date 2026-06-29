# =============================================================================
# RÔLE DE CE FICHIER DE TEST : test_loaders.py
# -----------------------------------------------------------------------------
# Ce fichier teste la couche "chargement de données" (loaders) du projet
# InduSense (maintenance prédictive industrielle). Concrètement, il valide :
#
#   1. La NORMALISATION DES IDENTIFIANTS de machine : on doit pouvoir lire
#      "M-2", "MACH_01", "M_07"... et toujours obtenir une forme canonique
#      unique ("MACH-02", "MACH-01", "MACH-07"). Sans cela, la même machine
#      physique apparaîtrait sous plusieurs noms et fausserait les jointures.
#
#   2. La CONSTRUCTION DU JEU DE DONNÉES final (build_dataset) :
#        - la cible "panne" doit être BINAIRE {0, 1} (problème de classification)
#          et avec un taux 0 < rate < 0.5 (classe positive minoritaire mais
#          présente : un dataset 100 % de pannes ou 0 % de pannes serait inutile).
#        - les colonnes attendues (machine, timestamp, temperature,
#          pressure_bar, panne) doivent bien être présentes.
#
#   3. L'ISOLATION DU MERGE PAR MACHINE (merge_asof "by=machine") :
#        - une machine ne doit JAMAIS hériter de la pression mesurée sur une
#          AUTRE machine. C'est un garde-fou essentiel : sans le "by=machine",
#          on rapprocherait n'importe quelle mesure temporellement proche,
#          même si elle provient d'un autre équipement.
#
# Ce que ce fichier GARANTIT : des identifiants propres, une cible bien formée,
# et un appariement temps-réel (as-of) strictement cloisonné par machine.
# =============================================================================

# Path sert à construire des chemins de fichiers indépendants de l'OS
# (Windows / Linux) : on évite d'écrire "data/sample" "à la main".
from pathlib import Path

# pandas : manipulation des tableaux (DataFrame) de mesures de capteurs.
import pandas as pd

# pytest : framework de test (paramétrage, vérification des exceptions, etc.).
import pytest

# On importe les fonctions à tester depuis le package indusense.
# Les regrouper dans un seul import rend la dépendance testée explicite.
from indusense.data.loaders import (
    build_dataset,  # assemble temp + pression + incidents -> dataset final
    load_incidents,  # lit le fichier des incidents (relevés de pannes)
    load_pressure,  # lit le fichier des mesures de pression (.tsv)
    load_temperature,  # lit le fichier des mesures de température (.csv)
    normalize_machine_id,  # met un identifiant machine sous forme canonique
)

# Chemin vers le dossier d'échantillons de test.
# __file__ = ce fichier de test ; .resolve() -> chemin absolu ;
# .parents[1] = on remonte d'un cran (de tests/ vers la racine du projet) ;
# puis on descend vers data/sample. Ces données servent aux tests "réels".
SAMPLE = Path(__file__).resolve().parents[1] / "data" / "sample"


# @pytest.mark.parametrize : on rejoue le MÊME test avec plusieurs jeux
# (raw -> expected). Cela évite de copier-coller cinq fonctions quasi identiques
# et documente clairement tous les formats d'entrée que l'on doit accepter.
@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("MACH-01", "MACH-01"),  # déjà canonique : doit rester inchangé
        ("MACH_01", "MACH-01"),  # underscore -> tiret (séparateur normalisé)
        ("M-06", "MACH-06"),  # préfixe court "M" -> "MACH" complet
        ("M-2", "MACH-02"),  # numéro 1 chiffre -> zéro-padding "02"
        ("M_07", "MACH-07"),  # underscore + préfixe court combinés
    ],
)
def test_normalize_machine_id_variants(raw, expected):
    # Intention : quel que soit le format d'entrée, la sortie doit être
    # la forme canonique attendue. C'est la garantie qu'une même machine
    # ne se retrouvera pas dédoublée sous plusieurs orthographes.
    assert normalize_machine_id(raw) == expected


def test_normalize_machine_id_without_number_raises():
    # Intention : un identifiant SANS numéro ("NOPE") est invalide.
    # On veut un échec FRANC (ValueError) plutôt qu'une normalisation
    # silencieuse hasardeuse : mieux vaut bloquer une donnée douteuse.
    with pytest.raises(ValueError):
        normalize_machine_id("NOPE")


def test_build_dataset_has_binary_target():
    # On charge les trois sources réelles d'échantillon : température,
    # pression et incidents. Chaque loader gère son propre format de fichier
    # (csv vs tsv) et renvoie un DataFrame normalisé.
    temp = load_temperature(SAMPLE / "capteurs_temperature.csv")
    pres = load_pressure(SAMPLE / "capteurs_pression.tsv")
    inc = load_incidents(SAMPLE / "releves_incidents.csv")

    # build_dataset assemble tout en un seul tableau "prêt pour le ML".
    # window_hours=24 : un incident "étiquette" les mesures dans une fenêtre
    # de 24 h (horizon de prédiction de la panne).
    dataset = build_dataset(temp, pres, inc, window_hours=24)

    # 1) Le dataset doit contenir AU MOINS ces colonnes (sous-ensemble <=).
    #    On vérifie le contrat de sortie : features + clé + cible présentes.
    assert {"machine", "timestamp", "temperature", "pressure_bar", "panne"} <= set(dataset.columns)
    # 2) La cible "panne" doit être strictement BINAIRE : uniquement 0 ou 1.
    #    set(...unique()) <= {0, 1} interdit toute autre valeur (2, NaN, "oui"...).
    assert set(dataset["panne"].unique()) <= {0, 1}
    # 3) Le taux de pannes (moyenne d'une colonne 0/1) doit être dans ]0 ; 0.5[ :
    #    > 0 -> il existe bien des pannes à apprendre ;
    #    < 0.5 -> la panne reste l'événement minoritaire (cas réaliste, classe
    #    positive rare). Hors de cet intervalle, le dataset serait inexploitable.
    assert 0 < dataset["panne"].mean() < 0.5


def test_merge_asof_never_matches_other_machine():
    # Ce test fabrique des données "piégées" à la main pour prouver le
    # cloisonnement par machine du merge_asof. On contrôle tout pour rendre
    # la fuite POSSIBLE si le code était mal écrit, puis on vérifie qu'elle
    # n'arrive pas.

    # Deux mesures de température, une par machine, presque au même instant.
    temp = pd.DataFrame(
        {
            "machine": ["MACH-01", "MACH-02"],
            "timestamp": pd.to_datetime(["2026-01-01 12:00", "2026-01-01 12:01"]),
            "temperature": [50.0, 60.0],
        }
    )
    # Mesures de pression "piégées" :
    #  - MACH-02 a une pression 180.0 à 12:00 (proche temporellement de tout) ;
    #  - MACH-01 a une pression 999.0 mais à 20:00 (8 h plus tard).
    # Si le merge ignorait la machine, MACH-01 (mesuré à 12:00) pourrait
    # capter par erreur le 180.0 de MACH-02 (valeur d'une AUTRE machine).
    pres = pd.DataFrame(
        {
            "machine": ["MACH-02", "MACH-01"],
            "timestamp": pd.to_datetime(["2026-01-01 12:00", "2026-01-01 20:00"]),
            "pressure_bar": [180.0, 999.0],
        }
    )
    # Aucun incident ici : on isole le comportement de la jointure des capteurs.
    inc = pd.DataFrame(columns=["machine", "incident_ts"])

    # tolerance_minutes=90 : merge_asof n'apparie une pression que si elle
    # tombe dans +/- 90 min de la mesure de température. La pression de MACH-01
    # (à 20:00) est trop lointaine (8 h) -> hors tolérance -> aucun appariement
    # -> la ligne MACH-01 est écartée. Reste seulement MACH-02 (180.0 à 12:00).
    dataset = build_dataset(temp, pres, inc, window_hours=24, tolerance_minutes=90)

    # On ne doit garder que MACH-02 : MACH-01 n'a aucune pression valide
    # DANS SA PROPRE série (et ne doit pas voler celle de MACH-02).
    assert list(dataset["machine"]) == ["MACH-02"]
    # La pression conservée pour MACH-02 est bien la sienne : 180.0.
    # C'est la preuve que "by=machine" empêche tout emprunt inter-machines.
    assert dataset.iloc[0]["pressure_bar"] == 180.0
