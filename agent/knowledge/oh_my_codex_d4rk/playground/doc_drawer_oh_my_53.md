dim,
        active_dimensions,
        inactive_value=inactive_value,
    )[:, active_dimensions]
    final_candidates = np.vstack([final_candidates, X_array])
    final_mu = gp.predict(final_candidates[:, active_dimensions])
    incumbent = final_candidates[int(np.argmax(final_mu))]

    resample_rng = np.random.default_rng(seed + 10_000)
    final_scores = np.array([noisy_objective(incumbent, resample_rng) for _ in range(final_resamples)], dtype=float)
    return {
        'algorithm': 'screened_bayesian_gp',
        'active_dimensions': active_dimensions,
        'best_observed': float(np.max(y_array)),
        'best_mean': float(final_scores.mean()),
        'best_std': float(final_scores.std(ddof=0)),
        'best_noiseless': float(noiseless_objective(incumbent)),