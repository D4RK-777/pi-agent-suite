from __future__ import annotations

import numpy as np

DIMENSION = 24
INFORMATIVE_DIMS = (1, 5, 11, 17)
NOISE_STD = 0.08


def validate_point(x: np.ndarray) -> np.ndarray:
    arr = np.asarray(x, dtype=float)
    if arr.shape != (DIMENSION,):
        raise ValueError(f"expected shape ({DIMENSION},), got {arr.shape}")
    return np.clip(arr, 0.0, 1.0)


def noiseless_objective(x: np.ndarray) -> float:
    x = validate_point(x)
    a = x[1]
    b = x[5]
    c = x[11]
    d = x[17]