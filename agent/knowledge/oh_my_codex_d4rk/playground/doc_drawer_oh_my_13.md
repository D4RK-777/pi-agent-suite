from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

CONFIG_PATH = Path(__file__).with_name('config.json')


@dataclass
class Metrics:
    comparisons: int = 0
    moves: int = 0

    def score(self) -> float:
        return self.comparisons + 0.35 * self.moves


class Ops:
    def __init__(self) -> None:
        self.metrics = Metrics()

    def compare(self, a: int, b: int) -> int:
        self.metrics.comparisons += 1
        return (a > b) - (a < b)

    def move(self, count: int = 1) -> None:
        self.metrics.moves += count


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text())