erved'))

    rng = np.random.default_rng(seed)
    X: list[np.ndarray] = []
    y: list[float] = []

    for _ in range(n_initial_random):
        x = sample_uniform(rng, 1, dim)[0]
        X.append(x)
        y.append(float(noisy_objective(x, rng)))

    X_array = np.asarray(X, dtype=float)
    y_array = np.asarray(y, dtype=float)
    active_dimensions = infer_active_dimensions(X_array, y_array, top_k)
    anchor = choose_anchor(X_array, y_array, anchor_mode)