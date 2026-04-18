peof v !== 'string')) {
    throw new Error('`allowed_modes` must be a non-empty string array');
  }

  const cooldown = parsed.cooldown_ms;
  const maxInjections = parsed.max_injections_per_session;
  if (typeof cooldown !== 'number' || cooldown < 0 || !Number.isFinite(cooldown)) {
    throw new Error('`cooldown_ms` must be a non-negative number');
  }
  if (typeof maxInjections !== 'number' || maxInjections < 1 || !Number.isFinite(maxInjections)) {
    throw new Error('`max_injections_per_session` must be >= 1');
  }