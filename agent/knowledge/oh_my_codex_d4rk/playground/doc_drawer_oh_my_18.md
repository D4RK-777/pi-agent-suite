.get('run_detection_min', 10))
    counting_span_limit = int(params.get('counting_span_limit', 128))

    if len(values) <= insertion_threshold:
        return insertion_sort(values, ops)
    if values:
        min_value = min(values)
        max_value = max(values)
        if max_value - min_value <= counting_span_limit:
            return counting_sort(values, min_value, max_value, ops)
    if longest_non_decreasing_run(values) >= run_detection_min:
        return insertion_sort(values, ops)
    return merge_sort(values, ops)


def baseline_sort(values: list[int], _config: dict, ops: Ops) -> list[int]:
    return merge_sort(values, ops)