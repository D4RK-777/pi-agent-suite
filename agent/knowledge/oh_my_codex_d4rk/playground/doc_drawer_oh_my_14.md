.metrics.moves += count


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text())


def insertion_sort(values: list[int], ops: Ops) -> list[int]:
    arr = values[:]
    for i in range(1, len(arr)):
        key = arr[i]
        ops.move()
        j = i - 1
        while j >= 0 and ops.compare(arr[j], key) > 0:
            arr[j + 1] = arr[j]
            ops.move()
            j -= 1
        arr[j + 1] = key
        ops.move()
    return arr