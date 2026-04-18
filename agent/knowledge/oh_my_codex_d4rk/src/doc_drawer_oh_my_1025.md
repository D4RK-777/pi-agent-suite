if (!existsSync(notifyHook)) {
    throw new Error(`notify-hook.js not found at ${notifyHook}`);
  }

  const threadId = `tmux-test-${Date.now()}`;
  const turnId = `turn-${Date.now()}`;
  const message = args.join(' ').trim() || 'tmux-hook test payload';
  const payload = {
    type: 'agent-turn-complete',
    cwd,
    'thread-id': threadId,
    'turn-id': turnId,
    'input-messages': ['omx tmux-hook test'],
    'last-assistant-message': message,
  };