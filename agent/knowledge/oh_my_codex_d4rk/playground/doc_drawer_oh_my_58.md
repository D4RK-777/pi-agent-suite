y) -> np.ndarray:
    x = validate_point(x)
    centered = x - 0.5
    return PROJECTION @ centered


def noiseless_objective(x: np.ndarray) -> float:
    z0, z1, z2, z3 = latent_coordinates(x)
    basin = 3.0 * np.exp(-((z0 - 0.11) ** 2) / 0.010 - ((z1 + 0.18) ** 2) / 0.016)
    ridge = 1.25 * np.exp(-((z2 - 0.04) ** 2) / 0.024)
    wave = 0.60 * np.cos(6.0 * np.pi * z3)
    interaction = 0.55 * np.sin(10.0 * (z0 + 0.5) * (z2 + 0.5)) + 0.40 * np.cos(8.0 * (z1 + 0.5) * (z3 + 0.5))
    penalties = 0.95 * (z0 - 0.11) ** 2 + 0.75 * (z1 + 0.18) ** 2 + 0.60 * (z2 - 0.04) ** 2 + 0.35 * (z3 - 0.07) ** 2
    return float(basin + ridge + wave + interaction - penalties)