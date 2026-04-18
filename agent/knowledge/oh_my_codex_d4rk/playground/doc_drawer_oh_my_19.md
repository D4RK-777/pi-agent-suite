e_sort(values: list[int], _config: dict, ops: Ops) -> list[int]:
    return merge_sort(values, ops)


def build_cases() -> list[tuple[str, list[int], float]]:
    cases: list[tuple[str, list[int], float]] = []
    sizes = [32, 64, 96]
    for n in sizes:
        cases.append((f'random-{n}', [((i * 37 + 11) % 101) for i in range(n)], 1.0))
        cases.append((f'reverse-{n}', list(range(n, 0, -1)), 1.1))
        cases.append((f'nearly-sorted-{n}', [i if i % 9 else max(0, i - 3) for i in range(n)], 1.2))
        cases.append((f'duplicates-{n}', [((i * 7) % 8) for i in range(n)], 1.3))
        cases.append((f'low-cardinality-{n}', [((i * 13 + 5) % 16) for i in range(n)], 1.15))
    return cases