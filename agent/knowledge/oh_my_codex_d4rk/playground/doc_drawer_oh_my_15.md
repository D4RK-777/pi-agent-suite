ops.move()
            j -= 1
        arr[j + 1] = key
        ops.move()
    return arr


def merge_sort(values: list[int], ops: Ops) -> list[int]:
    if len(values) <= 1:
        return values[:]
    mid = len(values) // 2
    left = merge_sort(values[:mid], ops)
    right = merge_sort(values[mid:], ops)
    out: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if ops.compare(left[i], right[j]) <= 0:
            out.append(left[i])
            ops.move()
            i += 1
        else:
            out.append(right[j])
            ops.move()
            j += 1
    if i < len(left):
        out.extend(left[i:])
        ops.move(len(left) - i)
    if j < len(right):
        out.extend(right[j:])
        ops.move(len(right) - j)
    return out