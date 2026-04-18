n(y) // 6):]]
        mean = elite.mean(axis=0)
        std = np.clip(elite.std(axis=0), 0.05, 0.25)

    X = np.vstack(all_points)
    y = np.concatenate(all_scores)
    incumbent = X[int(np.argmax(y))]
    resample_rng = np.random.default_rng(seed + 10_000)
    final_scores = np.array([noisy_objective(incumbent, resample_rng) for _ in range(final_resamples)], dtype=float)
    return {
        'algorithm': 'cem_search',
        'best_observed': float(np.max(y)),
        'best_mean': float(final_scores.mean()),
        'best_std': float(final_scores.std(ddof=0)),
        'best_noiseless': float(noiseless_objective(incumbent)),
        'incumbent': incumbent.tolist(),
    }