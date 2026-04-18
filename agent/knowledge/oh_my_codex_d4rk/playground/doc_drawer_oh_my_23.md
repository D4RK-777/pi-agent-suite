from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel

from problem import DIMENSION, NOISE_STD, noisy_objective, noiseless_objective

CONFIG_PATH = Path(__file__).with_name('config.json')


def load_config(path: str | None = None) -> dict[str, Any]:
    cfg_path = Path(path) if path else CONFIG_PATH
    return json.loads(cfg_path.read_text())


def sample_uniform(rng: np.random.Generator, n: int, dim: int = DIMENSION) -> np.ndarray:
    return rng.random((n, dim))