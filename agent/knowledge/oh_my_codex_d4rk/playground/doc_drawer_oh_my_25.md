lueError(f'active_dimensions must stay within [0, {dim})')
    return sorted(dict.fromkeys(active))


def sample_subspace_uniform(
    rng: np.random.Generator,
    n: int,
    dim: int,
    active_dimensions: list[int],
    inactive_value: float = 0.5,
) -> np.ndarray:
    points = np.full((n, dim), inactive_value, dtype=float)
    points[:, active_dimensions] = rng.random((n, len(active_dimensions)))
    return points