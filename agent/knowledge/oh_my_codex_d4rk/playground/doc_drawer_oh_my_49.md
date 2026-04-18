_resamples', 24))
    seed = int(config.get('seed', 23))
    params = dict(config.get('params', {}))

    n_initial_random = int(params.get('n_initial_random', 18))
    top_k = int(params.get('top_k', 6))
    candidate_pool_size = int(params.get('candidate_pool_size', 2500))
    final_candidate_pool_size = int(params.get('final_candidate_pool_size', max(candidate_pool_size, 5000)))
    acq_beta = float(params.get('acq_beta', 1.25))
    gp_length_scale = float(params.get('gp_length_scale', 0.22))
    inactive_value = float(params.get('inactive_value', 0.5))
    anchor_mode = str(params.get('anchor_mode', 'best_observed'))

    rng = np.random.default_rng(seed)
    X: list[np.ndarray] = []
    y: list[float] = []