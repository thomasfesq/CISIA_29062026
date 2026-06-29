from pathlib import Path

import pandas as pd
from pandas.testing import assert_series_equal

GOLD_PATH = Path(__file__).resolve().parents[1] / "data" / "gold" / "gold_dataset.csv"


def test_gold_dataset_temporal_features_use_only_past_values():
    """Validate temporal features already materialized in the gold dataset.

    The first rows per machine are skipped for each check because the starter gold
    dataset was generated after dropping the initial rows with unavailable history.
    For every later row, lag/rolling features must match values strictly before
    the current timestamp, machine by machine.
    """
    df = pd.read_csv(GOLD_PATH, parse_dates=["timestamp"])
    df = df.sort_values(["machine", "timestamp"]).reset_index(drop=True)

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
    assert required_cols <= set(df.columns)

    for _, machine_df in df.groupby("machine", sort=False):
        machine_df = machine_df.sort_values("timestamp").reset_index(drop=True)

        for source_col in ("temperature", "pressure_bar"):
            for lag in (1, 3, 6):
                expected = machine_df[source_col].shift(lag)
                actual = machine_df[f"{source_col}_lag{lag}"]
                mask = expected.notna()
                assert_series_equal(
                    actual[mask].reset_index(drop=True),
                    expected[mask].reset_index(drop=True),
                    check_names=False,
                    rtol=1e-10,
                    atol=1e-10,
                )

            for window in (3, 6):
                expected = machine_df[source_col].shift(1).rolling(window).mean()
                actual = machine_df[f"{source_col}_roll{window}_mean"]
                mask = expected.notna()
                assert_series_equal(
                    actual[mask].reset_index(drop=True),
                    expected[mask].reset_index(drop=True),
                    check_names=False,
                    rtol=1e-10,
                    atol=1e-10,
                )


def test_gold_dataset_has_no_incident_columns_as_features():
    """Incident fields are labels/provenance, never prediction-time features."""
    df = pd.read_csv(GOLD_PATH, nrows=1)
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
    assert forbidden_cols.isdisjoint(df.columns)
