': turnId,
    'input-messages': ['omx tmux-hook test'],
    'last-assistant-message': message,
  };

  const result = spawnSync(process.execPath, [notifyHook, JSON.stringify(payload)], {
    cwd,
    encoding: 'utf-8',
      windowsHide: true,
    });
  if (result.error) {
    throw new Error(`failed to run notify-hook: ${result.error.message}`);
  }
  if (result.status !== 0) {
    throw new Error(`notify-hook exited ${result.status}: ${(result.stderr || result.stdout || '').trim()}`);
  }

  console.log('tmux-hook test: notify-hook executed.');
  console.log(`thread_id=${threadId}`);
  console.log(`turn_id=${turnId}`);
  console.log('Check: .omx/logs/tmux-hook-YYYY-MM-DD.jsonl for skip/reason codes.');
}