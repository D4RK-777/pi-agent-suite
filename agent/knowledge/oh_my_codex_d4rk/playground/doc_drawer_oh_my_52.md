t(candidate_points[:, active_dimensions], return_std=True)
        acquisition = mu + acq_beta * std
        x_next = candidate_points[int(np.argmax(acquisition))]
        X.append(x_next)
        y.append(float(noisy_objective(x_next, rng)))

    X_array = np.asarray(X, dtype=float)
    y_array = np.asarray(y, dtype=float)
    gp = fit_gp(X_array[:, active_dimensions], y_array, length_scale=gp_length_scale)
    final_candidate_rng = np.random.default_rng(seed + 12_345)
    final_candidates = np.tile(anchor, (final_candidate_pool_size, 1))
    final_candidates[:, active_dimensions] = sample_subspace_uniform(
        final_candidate_rng,
        final_candidate_pool_size,
        dim,
        active_dimensions,
        inactive_value=inactive_value,
    )[:, active_dimensions]