if j < len(right):
        out.extend(right[j:])
        ops.move(len(right) - j)
    return out


def counting_sort(values: list[int], min_value: int, max_value: int, ops: Ops) -> list[int]:
    offset = min_value
    counts = [0] * (max_value - min_value + 1)
    ops.move(len(counts))
    for value in values:
        counts[value - offset] += 1
        ops.move()
    out: list[int] = []
    for index, count in enumerate(counts):
        if count:
            value = index + offset
            out.extend([value] * count)
            ops.move(count)
    return out