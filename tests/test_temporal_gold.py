# =============================================================================
# RÔLE DE CE FICHIER DE TEST : test_temporal_gold.py
# -----------------------------------------------------------------------------
# Ce fichier valide le "GOLD DATASET" : le jeu de données FINAL, déjà calculé
# et figé sur disque (data/gold/gold_dataset.csv), celui qui servira à
# entraîner le modèle. On ne recalcule pas tout : on VÉRIFIE que ce qui a été
# matérialisé respecte bien les règles anti-fuite.
#
# Deux garanties essentielles sont contrôlées ici :
#
#   1. ANTI-FUITE TEMPORELLE des features (lags et moyennes glissantes) :
#      pour chaque machine, chaque feature lagN / rollN doit correspondre
#      EXACTEMENT à des valeurs strictement ANTÉRIEURES au timestamp courant.
#      - lagN = valeur d'il y a N pas (shift(N)).
#      - rollN_mean = moyenne glissante sur N valeurs PASSÉES, donc shift(1)
#        AVANT rolling (jamais la valeur courante = ce serait une fuite).
#      On recalcule la "vérité attendue" et on la compare à ce qui est stocké.
#
#   2. ABSENCE DES COLONNES D'INCIDENT comme features :
#      les champs liés à l'incident (incident_id, severity, comment, date,
#      time, shift, opérateur...) décrivent la PANNE elle-même (la cible) ou
#      sa provenance. Les utiliser comme variables d'entrée serait une FUITE
#      DE LA CIBLE (target leakage) : au moment de prédire, on ne connaît pas
#      encore l'incident. Le gold dataset ne doit donc contenir AUCUNE de ces
#      colonnes côté features.
#
# Ce que ce fichier GARANTIT : le dataset d'entraînement est "honnête" — il
# ne regarde ni le futur, ni la réponse.
# =============================================================================

# Path : pour localiser le fichier gold de façon portable (Windows/Linux).
from pathlib import Path

# pandas : lecture du CSV et reconstruction des features de référence.
import pandas as pd

# assert_series_equal : comparaison rigoureuse de deux séries pandas
# (valeurs, alignement), avec tolérances numériques paramétrables.
from pandas.testing import assert_series_equal

# Chemin vers le gold dataset : on remonte de tests/ vers la racine du projet
# (.parents[1]) puis on descend dans data/gold/gold_dataset.csv.
GOLD_PATH = Path(__file__).resolve().parents[1] / "data" / "gold" / "gold_dataset.csv"


def test_gold_dataset_temporal_features_use_only_past_values():
    """Valide les features temporelles déjà matérialisées dans le gold dataset.

    Les premières lignes de chaque machine sont ignorées à chaque vérification,
    car le gold dataset de départ a été généré après suppression des lignes
    initiales dont l'historique n'était pas disponible. Pour toute ligne
    ultérieure, les features de lag/rolling doivent correspondre à des valeurs
    strictement antérieures au timestamp courant, machine par machine.
    """
    # On lit le gold dataset en convertissant la colonne timestamp en dates
    # réelles (parse_dates) pour pouvoir trier chronologiquement.
    df = pd.read_csv(GOLD_PATH, parse_dates=["timestamp"])
    # Tri global par (machine, timestamp) puis réindexation propre.
    # Indispensable avant tout calcul de lag/rolling : l'ordre temporel par
    # machine est la base de l'anti-fuite.
    df = df.sort_values(["machine", "timestamp"]).reset_index(drop=True)

    # Contrat de colonnes attendu dans le gold dataset : la clé (machine,
    # timestamp), les deux signaux bruts (temperature, pressure_bar) et toutes
    # les features dérivées (lags 1/3/6 et moyennes glissantes 3/6).
    required_cols = {
        "machine",
        "timestamp",
        "temperature",
        "pressure_bar",
        "temperature_lag1",
        "temperature_lag3",
        "temperature_lag6",
        "temperature_roll3_mean",
        "temperature_roll6_mean",
        "pressure_bar_lag1",
        "pressure_bar_lag3",
        "pressure_bar_lag6",
        "pressure_bar_roll3_mean",
        "pressure_bar_roll6_mean",
    }
    # Toutes ces colonnes doivent être présentes (sous-ensemble <= colonnes réelles).
    assert required_cols <= set(df.columns)

    # On traite CHAQUE machine séparément. sort=False garde l'ordre d'apparition
    # des groupes ; ce qui compte, c'est qu'on ne mélange jamais deux machines.
    for _, machine_df in df.groupby("machine", sort=False):
        # Au sein de la machine, on re-trie par temps et on réindexe : ainsi
        # shift()/rolling() opèrent sur une série purement chronologique.
        machine_df = machine_df.sort_values("timestamp").reset_index(drop=True)

        # On vérifie indépendamment les deux signaux source.
        for source_col in ("temperature", "pressure_bar"):
            # --- Vérification des LAGS (1, 3, 6) ---
            for lag in (1, 3, 6):
                # Vérité attendue : la valeur d'il y a "lag" pas = shift(lag).
                # shift décale vers le bas, donc on récupère bien le PASSÉ.
                expected = machine_df[source_col].shift(lag)
                # Valeur réellement stockée dans le gold dataset.
                actual = machine_df[f"{source_col}_lag{lag}"]
                # Les premières lignes n'ont pas assez de passé -> NaN dans
                # "expected". On les exclut via un masque (on ne compare que
                # là où une valeur passée existe réellement).
                mask = expected.notna()
                # Comparaison stricte des deux séries sur les lignes valides.
                # reset_index(drop=True) aligne les positions après masquage ;
                # check_names=False ignore le nom de la série (seules les valeurs
                # comptent) ; rtol/atol = tolérance numérique minime pour les
                # flottants (égalité "à epsilon près").
                assert_series_equal(
                    actual[mask].reset_index(drop=True),
                    expected[mask].reset_index(drop=True),
                    check_names=False,
                    rtol=1e-10,
                    atol=1e-10,
                )

            # --- Vérification des MOYENNES GLISSANTES (fenêtres 3 et 6) ---
            for window in (3, 6):
                # Vérité attendue : shift(1) AVANT rolling -> la fenêtre ne
                # contient que des valeurs STRICTEMENT passées (jamais la valeur
                # courante). C'est exactement la règle anti-fuite : sans le
                # shift(1), la moyenne inclurait l'instant présent = fuite.
                expected = machine_df[source_col].shift(1).rolling(window).mean()
                # Valeur réellement stockée pour cette moyenne glissante.
                actual = machine_df[f"{source_col}_roll{window}_mean"]
                # On exclut les lignes où la fenêtre n'est pas encore complète
                # (NaN tant qu'il n'y a pas "window" valeurs passées disponibles).
                mask = expected.notna()
                # Même comparaison rigoureuse que pour les lags.
                assert_series_equal(
                    actual[mask].reset_index(drop=True),
                    expected[mask].reset_index(drop=True),
                    check_names=False,
                    rtol=1e-10,
                    atol=1e-10,
                )


def test_gold_dataset_has_no_incident_columns_as_features():
    """Les champs d'incident sont des labels/provenance, jamais des features
    au moment de la prédiction."""
    # On ne lit qu'UNE seule ligne (nrows=1) : il suffit de connaître les
    # noms de colonnes, pas leur contenu. C'est rapide et économe.
    df = pd.read_csv(GOLD_PATH, nrows=1)
    # Liste NOIRE des colonnes interdites côté features : elles décrivent la
    # panne (severity, comment...), son horodatage (date, time), le poste
    # (shift) ou l'opérateur. Présentes en entrée, elles renseigneraient le
    # modèle sur la réponse -> fuite de la cible.
    forbidden_cols = {
        "incident_id",
        "severity",
        "operator_name",
        "operator_badge",
        "comment",
        "date",
        "time",
        "shift",
    }
    # isdisjoint = aucune intersection : AUCUNE colonne interdite ne doit
    # figurer dans le gold dataset. Si l'une apparaissait, le test échouerait
    # et signalerait une fuite potentielle de la cible.
    assert forbidden_cols.isdisjoint(df.columns)
