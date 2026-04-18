04) ** 2 + 0.35 * (z3 - 0.07) ** 2
    return float(basin + ridge + wave + interaction - penalties)


def noisy_objective(x: np.ndarray, rng: np.random.Generator) -> float:
    return noiseless_objective(x) + float(rng.normal(0.0, NOISE_STD))