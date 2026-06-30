# =============================================================================
# RÔLE DE CE FICHIER DE TEST : test_temporal.py
# -----------------------------------------------------------------------------
# Ce fichier teste la FABRICATION DES FEATURES TEMPORELLES
# (add_temporal_features) : retards (lags) et moyennes glissantes (rolling).
# Ces variables résument le PASSÉ d'une machine pour prédire sa future panne.
#
# Le point capital ici, c'est l'ANTI-FUITE TEMPORELLE (temporal leakage) :
#
#   - Un "lag1" = la valeur de l'instant PRÉCÉDENT. Pour la TOUTE PREMIÈRE
#     ligne d'une machine, il n'existe pas de passé : le lag1 vaut donc NaN.
#     C'est NORMAL et VOULU : on ne peut pas inventer une histoire qui n'a pas
#     encore eu lieu.
#
#   - Une moyenne glissante doit se calculer avec shift(1) AVANT le rolling,
#     c'est-à-dire UNIQUEMENT sur des valeurs strictement passées. Inclure la
#     valeur courante serait une FUITE : au moment de prédire, on utiliserait
#     une information qu'on n'aurait pas encore en production.
#
#   - Le calcul doit être fait MACHINE PAR MACHINE et dans l'ORDRE CHRONOLOGIQUE.
#     Trier par (machine, timestamp) empêche qu'une machine hérite du passé
#     d'une autre, et empêche un "futur" de se glisser avant un "passé".
#
# Ce que ce fichier GARANTIT : les features temporelles ne regardent jamais le
# présent ni le futur, sont cloisonnées par machine, et échouent proprement si
# une colonne source manque.
# =============================================================================

# pandas pour construire les DataFrames de test et manipuler les séries.
import pandas as pd

# pytest pour vérifier qu'une erreur attendue (ValueError) est bien levée.
import pytest

# Fonction testée : ajoute les colonnes de lags et de moyennes glissantes.
from indusense.features.temporal import add_temporal_features


def test_temporal_features_do_not_use_current_value():
    # Une seule machine, 4 instants consécutifs (fréquence horaire "h").
    # Valeurs simples et croissantes pour rendre les calculs vérifiables à la main.
    df = pd.DataFrame(
        {
            "machine": ["MACH-01"] * 4,
            "timestamp": pd.date_range("2025-01-01", periods=4, freq="h"),
            "temperature": [10.0, 20.0, 30.0, 40.0],
            "pressure_bar": [195.0, 196.0, 197.0, 198.0],
        }
    )
    # On demande : lag de 1 (valeur précédente) et fenêtre glissante de 2,
    # uniquement sur la colonne "temperature".
    out = add_temporal_features(df, value_cols=("temperature",), lags=(1,), windows=(2,))

    # 1re ligne : aucun passé disponible -> le lag1 DOIT être NaN.
    # .isna().iloc[0] vérifie précisément que la première valeur est manquante.
    # C'est la preuve qu'on n'invente pas une valeur antérieure inexistante.
    assert out["temperature_lag1"].isna().iloc[0]
    # 3e ligne (index 2) : moyenne glissante de fenêtre 2 calculée sur le PASSÉ.
    # Grâce au shift(1), elle porte sur les valeurs des index 0 et 1 (10 et 20),
    # PAS sur la valeur courante 30. Donc (10 + 20) / 2 = 15.0.
    # Si la valeur courante était (à tort) incluse, on aurait (20 + 30)/2 = 25 : fuite.
    assert out["temperature_roll2_mean"].iloc[2] == 15.0


def test_temporal_features_sort_by_machine_and_time():
    # Données VOLONTAIREMENT mélangées (lignes pas dans l'ordre temporel,
    # machines entrelacées) pour vérifier que la fonction trie correctement
    # par (machine, timestamp) avant de calculer les features.
    df = pd.DataFrame(
        {
            "machine": ["MACH-01", "MACH-02", "MACH-01", "MACH-02"],
            "timestamp": pd.to_datetime(
                ["2025-01-01 01:00", "2025-01-01 00:00", "2025-01-01 00:00", "2025-01-01 01:00"]
            ),
            "temperature": [11.0, 20.0, 10.0, 21.0],
            "pressure_bar": [196.0, 205.0, 195.0, 206.0],
        }
    )
    out = add_temporal_features(df, value_cols=("temperature",), lags=(1,), windows=(2,))

    # On isole les lignes de MACH-01 et on réindexe proprement (0, 1, ...).
    # reset_index(drop=True) jette l'ancien index pour pouvoir cibler .loc[1].
    m1 = out[out["machine"] == "MACH-01"].reset_index(drop=True)
    # Pour MACH-01, l'ordre chronologique est : 00:00 (temp 10) puis 01:00 (temp 11).
    # Le lag1 de la 2e ligne (01:00) doit donc valoir 10.0 = la valeur précédente
    # de CETTE machine. Cela prouve que le tri par machine + temps a bien eu lieu
    # (sinon le lag serait faux, voire emprunté à MACH-02).
    assert m1.loc[1, "temperature_lag1"] == 10.0


def test_temporal_features_missing_column_raises():
    # DataFrame sans colonne "temperature" : la feature demandée est impossible.
    df = pd.DataFrame({"machine": ["MACH-01"], "timestamp": pd.to_datetime(["2025-01-01"])})
    # Intention : on exige un échec EXPLICITE (ValueError) quand une colonne
    # source manque, plutôt qu'une création silencieuse de colonnes vides
    # (qui passerait inaperçue et corromprait l'entraînement).
    with pytest.raises(ValueError):
        add_temporal_features(df, value_cols=("temperature",))
