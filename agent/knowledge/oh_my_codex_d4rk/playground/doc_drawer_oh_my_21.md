pend({'case': name, 'weighted_cost': weighted})
    return {'total_cost': total, 'cases': per_case}


def run_config(config: dict) -> dict:
    algorithm_name = config.get('algorithm', 'hybrid_sort')
    if algorithm_name == 'hybrid_sort':
        result = evaluate_algorithm(hybrid_sort, config)
    elif algorithm_name == 'baseline_sort':
        result = evaluate_algorithm(baseline_sort, config)
    else:
        raise ValueError(f'unsupported algorithm: {algorithm_name}')
    result['algorithm'] = algorithm_name
    return result


def main() -> None:
    print(json.dumps(run_config(load_config())))


if __name__ == '__main__':
    main()