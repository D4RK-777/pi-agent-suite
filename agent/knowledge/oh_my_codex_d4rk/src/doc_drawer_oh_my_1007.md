arsed.skip_if_scrolling !== false) {
    throw new Error('`skip_if_scrolling` must be boolean');
  }

  return {
    enabled: parsed.enabled,
    target: { type: targetObj.type, value: targetObj.value },
    allowed_modes: allowedModes,
    cooldown_ms: cooldown,
    max_injections_per_session: maxInjections,
    prompt_template: promptTemplate,
    marker,
    dry_run: parsed.dry_run,
    log_level: parsed.log_level,
    skip_if_scrolling: parsed.skip_if_scrolling === false ? false : true,
  };
}