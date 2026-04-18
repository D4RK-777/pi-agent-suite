= index + offset
            out.extend([value] * count)
            ops.move(count)
    return out


def longest_non_decreasing_run(values: list[int]) -> int:
    if not values:
        return 0
    best = current = 1
    for idx in range(1, len(values)):
        if values[idx - 1] <= values[idx]:
            current += 1
        else:
            best = max(best, current)
            current = 1
    return max(best, current)


def hybrid_sort(values: list[int], config: dict, ops: Ops) -> list[int]:
    params = dict(config.get('params', {}))
    insertion_threshold = int(params.get('insertion_threshold', 12))
    run_detection_min = int(params.get('run_detection_min', 10))
    counting_span_limit = int(params.get('counting_span_limit', 128))