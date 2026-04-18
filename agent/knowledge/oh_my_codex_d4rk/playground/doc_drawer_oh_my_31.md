sions'))

    rng = np.random.default_rng(seed)
    X: list[np.ndarray] = []
    y: list[float] = []

    while len(X) < budget:
        if len(X) < n_initial_random:
            x_next = sample_subspace_uniform(rng, 1, dim, active_dimensions, inactive_value=inactive_value)[0]
        else:
            X_array = np.asarray(X, dtype=float)
            y_array = np.asarray(y, dtype=float)
            gp = fit_gp(X_array[:, active_dimensions], y_array, length_scale=gp_length_scale)
            candidate_points = sample_subspace_uniform(
                rng,
                candidate_pool_size,
                dim,
                active_dimensions,
                inactive_value=inactive_value,
            )