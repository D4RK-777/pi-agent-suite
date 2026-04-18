itResult?.usedPlaceholderTarget) {
    return;
  }
  const resolved = resolveValidateTarget(config);

  if (!resolved.ok) {
    throw new Error(`tmux target validation failed: ${resolved.reason}`);
  }

  console.log('tmux-hook config is valid.');
  console.log(`Resolved target pane: ${resolved.target}`);
  console.log(`Mode gating: ${config.allowed_modes.join(', ')}`);
  if (!config.enabled) {
    console.log('Note: config is currently disabled (`enabled: false`).');
  }
}