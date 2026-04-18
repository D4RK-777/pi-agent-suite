es.append((f'low-cardinality-{n}', [((i * 13 + 5) % 16) for i in range(n)], 1.15))
    return cases


def evaluate_algorithm(algorithm: Callable[[list[int], dict, Ops], list[int]], config: dict) -> dict:
    total = 0.0
    per_case = []
    for name, values, weight in build_cases():
        ops = Ops()
        out = algorithm(values, config, ops)
        if out != sorted(values):
            raise AssertionError(f'incorrect sort output for {name}')
        weighted = weight * ops.metrics.score()
        total += weighted
        per_case.append({'case': name, 'weighted_cost': weighted})
    return {'total_cost': total, 'cases': per_case}