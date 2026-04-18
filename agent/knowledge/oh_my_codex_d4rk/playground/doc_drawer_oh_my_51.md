active_dimensions(X_array, y_array, top_k)
    anchor = choose_anchor(X_array, y_array, anchor_mode)

    while len(X) < budget:
        X_array = np.asarray(X, dtype=float)
        y_array = np.asarray(y, dtype=float)
        gp = fit_gp(X_array[:, active_dimensions], y_array, length_scale=gp_length_scale)
        candidate_points = np.tile(anchor, (candidate_pool_size, 1))
        candidate_points[:, active_dimensions] = sample_subspace_uniform(
            rng,
            candidate_pool_size,
            dim,
            active_dimensions,
            inactive_value=inactive_value,
        )[:, active_dimensions]
        mu, std = gp.predict(candidate_points[:, active_dimensions], return_std=True)
        acquisition = mu + acq_beta * std