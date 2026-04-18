t_noiseless': float(noiseless_objective(incumbent)),
        'incumbent': incumbent.tolist(),
    }


def run_cem_search(config: dict[str, Any]) -> dict[str, Any]:
    dim = int(config.get('dimension', DIMENSION))
    budget = int(config.get('budget', 64))
    final_resamples = int(config.get('final_resamples', 24))
    seed = int(config.get('seed', 23))
    params = dict(config.get('params', {}))
    batch_size = int(params.get('cem_batch_size', 8))
    rng = np.random.default_rng(seed)

    mean = np.full(dim, 0.5, dtype=float)
    std = np.full(dim, 0.28, dtype=float)
    all_points: list[np.ndarray] = []
    all_scores: list[float] = []