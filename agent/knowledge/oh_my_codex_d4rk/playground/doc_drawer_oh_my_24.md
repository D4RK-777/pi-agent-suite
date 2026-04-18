: np.random.Generator, n: int, dim: int = DIMENSION) -> np.ndarray:
    return rng.random((n, dim))


def resolve_active_dimensions(dim: int, raw: Any) -> list[int]:
    if raw is None:
        return list(range(dim))
    active = [int(v) for v in raw]
    if not active:
        raise ValueError('active_dimensions cannot be empty')
    if any(v < 0 or v >= dim for v in active):
        raise ValueError(f'active_dimensions must stay within [0, {dim})')
    return sorted(dict.fromkeys(active))