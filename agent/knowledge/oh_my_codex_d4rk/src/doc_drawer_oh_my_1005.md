ber.isFinite(maxInjections)) {
    throw new Error('`max_injections_per_session` must be >= 1');
  }

  const promptTemplate = parsed.prompt_template;
  const marker = parsed.marker;
  if (typeof promptTemplate !== 'string' || promptTemplate.trim() === '') {
    throw new Error('`prompt_template` must be a non-empty string');
  }
  if (typeof marker !== 'string' || marker.trim() === '') {
    throw new Error('`marker` must be a non-empty string');
  }