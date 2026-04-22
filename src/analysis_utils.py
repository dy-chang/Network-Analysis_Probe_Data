from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import pandas as pd


@dataclass(frozen=True)
class ScenarioWindow:
    name: str
    before_start: str
    before_end: str
    after_start: str
    after_end: str


IMMEDIATE = ScenarioWindow(
    name="Immediate",
    before_start="2024-02-26",
    before_end="2024-03-25",
    after_start="2024-03-26",
    after_end="2024-04-25",
)

FALL = ScenarioWindow(
    name="Fall",
    before_start="2023-09-01",
    before_end="2023-11-30",
    after_start="2024-09-01",
    after_end="2024-11-30",
)

WINTER = ScenarioWindow(
    name="Winter",
    before_start="2023-12-01",
    before_end="2024-02-28",
    after_start="2024-12-01",
    after_end="2025-02-28",
)


def load_and_prepare_data(csv_path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df["local_datetime"] = pd.to_datetime(df["local_datetime"])
    df["Date"] = pd.to_datetime(df["local_datetime"].dt.date)
    df["Hour"] = df["local_datetime"].dt.hour
    if "Weekday" not in df.columns:
        df["Weekday"] = df["local_datetime"].dt.day_name()
    return df


def classify_peak(hour: int) -> str:
    if 7 <= hour < 10:
        return "AM Peak"
    if 16 <= hour < 19:
        return "PM Peak"
    return "Off-Peak"


def add_peak_column(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["Peak"] = out["Hour"].apply(classify_peak)
    return out


def filter_two_period_window(df: pd.DataFrame, scenario: ScenarioWindow) -> pd.DataFrame:
    before = (df["Date"] >= pd.Timestamp(scenario.before_start)) & (df["Date"] <= pd.Timestamp(scenario.before_end))
    after = (df["Date"] >= pd.Timestamp(scenario.after_start)) & (df["Date"] <= pd.Timestamp(scenario.after_end))
    out = df[before | after].copy()
    out["Period"] = out["Date"] < pd.Timestamp(scenario.after_start)
    out["Period"] = out["Period"].map({True: "Before", False: "After"})
    return out


def top_impacted_routes(df: pd.DataFrame, quantile: float = 0.80) -> list:
    route_delta = df.groupby(["Route_Number", "Period"])["tti_freeflow"].mean().unstack()
    route_delta["Delta_TTI"] = route_delta["After"] - route_delta["Before"]
    threshold = route_delta["Delta_TTI"].quantile(quantile)
    return route_delta[route_delta["Delta_TTI"] >= threshold].index.tolist()
