'best_mean': float(final_scores.mean()),
        'best_std': float(final_scores.std(ddof=0)),
        'best_noiseless': float(noiseless_objective(incumbent)),
        'incumbent': incumbent.tolist(),
    }


def run_search(config: dict[str, Any]) -> dict[str, Any]:
    algorithm = config.get('algorithm', 'random_search')
    if algorithm == 'random_search':
        return run_random_search(config)
    if algorithm == 'bayesian_gp':
        return run_bayesian_gp(config)
    raise ValueError(f'Unsupported algorithm: {algorithm}')