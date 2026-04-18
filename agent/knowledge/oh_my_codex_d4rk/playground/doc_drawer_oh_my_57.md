.03],
], dtype=float)
PROJECTION = _PROJECTION / np.linalg.norm(_PROJECTION, axis=1, keepdims=True)


def validate_point(x: np.ndarray) -> np.ndarray:
    arr = np.asarray(x, dtype=float)
    if arr.shape != (DIMENSION,):
        raise ValueError(f"expected shape ({DIMENSION},), got {arr.shape}")
    return np.clip(arr, 0.0, 1.0)


def latent_coordinates(x: np.ndarray) -> np.ndarray:
    x = validate_point(x)
    centered = x - 0.5
    return PROJECTION @ centered