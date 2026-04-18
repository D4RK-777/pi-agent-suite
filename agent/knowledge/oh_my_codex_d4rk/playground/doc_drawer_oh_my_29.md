t_noiseless': float(noiseless_objective(incumbent)),
        'incumbent': incumbent.tolist(),
    }


def run_bayesian_gp(config: dict[str, Any]) -> dict[str, Any]:
    dim = int(config.get('dimension', DIMENSION))
    budget = int(config.get('budget', 48))
    final_resamples = int(config.get('final_resamples', 24))
    seed = int(config.get('seed', 17))
    params = dict(config.get('params', {}))