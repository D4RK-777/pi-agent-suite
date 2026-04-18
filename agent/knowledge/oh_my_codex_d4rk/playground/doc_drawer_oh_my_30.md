_resamples', 24))
    seed = int(config.get('seed', 17))
    params = dict(config.get('params', {}))

    n_initial_random = int(params.get('n_initial_random', 10))
    candidate_pool_size = int(params.get('candidate_pool_size', 1500))
    final_candidate_pool_size = int(params.get('final_candidate_pool_size', max(candidate_pool_size, 4000)))
    acq_beta = float(params.get('acq_beta', 1.5))
    gp_length_scale = float(params.get('gp_length_scale', 0.18))
    inactive_value = float(params.get('inactive_value', 0.5))
    active_dimensions = resolve_active_dimensions(dim, params.get('active_dimensions'))

    rng = np.random.default_rng(seed)
    X: list[np.ndarray] = []
    y: list[float] = []