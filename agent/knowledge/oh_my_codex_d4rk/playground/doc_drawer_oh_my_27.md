alpha=1e-6,
        random_state=0,
        optimizer=None,
    )
    gp.fit(X, y)
    return gp


def run_random_search(config: dict[str, Any]) -> dict[str, Any]:
    dim = int(config.get('dimension', DIMENSION))
    budget = int(config.get('budget', 48))
    final_resamples = int(config.get('final_resamples', 24))
    seed = int(config.get('seed', 17))
    rng = np.random.default_rng(seed)

    points = sample_uniform(rng, budget, dim)
    observations = np.array([noisy_objective(point, rng) for point in points], dtype=float)
    incumbent_index = int(np.argmax(observations))
    incumbent = points[incumbent_index]