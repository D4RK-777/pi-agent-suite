reated: true,
    usedPlaceholderTarget: !detected,
    detectedSession: detected?.sessionName,
  };

  if (!silent) {
    console.log(`Created ${configPath}`);
    console.log('Feature is enabled by default (`"enabled": true`).');
    if (detected) {
      console.log(`Detected target: ${detected.target.type}:${detected.target.value}`);
    }
    if (detected?.sessionName) {
      console.log(`Detected tmux session: ${detected.sessionName}`);
    }
    if (!detected) {
      console.log('No running tmux target detected. Update `target.value` when ready.');
    }
  }

  return result;
}