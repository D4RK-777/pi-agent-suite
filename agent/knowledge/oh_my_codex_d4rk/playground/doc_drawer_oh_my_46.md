.full(dim, 0.28, dtype=float)
    all_points: list[np.ndarray] = []
    all_scores: list[float] = []

    for offset in range(0, budget, batch_size):
        current_batch = min(batch_size, budget - offset)
        if offset == 0:
            points = sample_uniform(rng, current_batch, dim)
        else:
            points = np.clip(rng.normal(mean, std, size=(current_batch, dim)), 0.0, 1.0)

        scores = np.array([noisy_objective(point, rng) for point in points], dtype=float)
        all_points.append(points)
        all_scores.append(scores)

        X = np.vstack(all_points)
        y = np.concatenate(all_scores)
        elite = X[np.argsort(y)[-max(4, len(y) // 6):]]
        mean = elite.mean(axis=0)
        std = np.clip(elite.std(axis=0), 0.05, 0.25)