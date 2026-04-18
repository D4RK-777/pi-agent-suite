& targetObj.type !== 'pane') {
    throw new Error('`target.type` must be "session" or "pane"');
  }
  if (typeof targetObj.value !== 'string' || targetObj.value.trim() === '') {
    throw new Error('`target.value` must be a non-empty string');
  }

  const allowedModes = parsed.allowed_modes;
  if (!Array.isArray(allowedModes) || allowedModes.length === 0 || allowedModes.some(v => typeof v !== 'string')) {
    throw new Error('`allowed_modes` must be a non-empty string array');
  }