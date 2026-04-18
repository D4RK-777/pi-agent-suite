float)
    points[:, active_dimensions] = rng.random((n, len(active_dimensions)))
    return points


def fit_gp(X: np.ndarray, y: np.ndarray, length_scale: float = 0.18) -> GaussianProcessRegressor:
    kernel = (
        ConstantKernel(1.0, constant_value_bounds='fixed')
        * Matern(length_scale=np.full(X.shape[1], length_scale), length_scale_bounds='fixed', nu=2.5)
        + WhiteKernel(noise_level=NOISE_STD ** 2, noise_level_bounds='fixed')
    )
    gp = GaussianProcessRegressor(
        kernel=kernel,
        normalize_y=True,
        alpha=1e-6,
        random_state=0,
        optimizer=None,
    )
    gp.fit(X, y)
    return gp