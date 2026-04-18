alpha=1e-6,
        random_state=0,
        optimizer=None,
    )
    gp.fit(X, y)
    return gp


def infer_active_dimensions(X: np.ndarray, y: np.ndarray, top_k: int) -> list[int]:
    X_centered = X - X.mean(axis=0, keepdims=True)
    y_centered = y - y.mean()
    scale = np.maximum(np.std(X_centered, axis=0), 1e-8)
    standardized = X_centered / scale
    coeffs, *_ = np.linalg.lstsq(standardized, y_centered, rcond=None)
    order = np.argsort(np.abs(coeffs))[-top_k:]
    return sorted(int(idx) for idx in order)


def choose_anchor(X: np.ndarray, y: np.ndarray, mode: str) -> np.ndarray:
    if mode == 'center':
        return np.full(X.shape[1], 0.5, dtype=float)
    return X[int(np.argmax(y))].copy()