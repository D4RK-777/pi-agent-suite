from __future__ import annotations

import json
from pathlib import Path

from sklearn.ensemble import ExtraTreesClassifier, HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

CONFIG_PATH = Path(__file__).with_name("config.json")


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text())


def build_model(config: dict):
    model_name = config.get("model", "decision_tree")
    params = dict(config.get("params", {}))