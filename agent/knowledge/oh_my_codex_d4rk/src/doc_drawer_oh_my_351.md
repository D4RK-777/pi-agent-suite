eturn false;
  }
  return !BLOCKED_EVALUATOR_PATTERNS.some((pattern) => pattern.test(normalized));
}

function buildLaunchReadinessSection(launchReady: boolean, blockedReasons: readonly string[]): string {
  if (launchReady) {
    return 'Launch-ready: yes\n- Evaluator command is concrete and can be compiled into sandbox.md';
  }

  return [
    'Launch-ready: no',
    ...blockedReasons.map((reason) => `- ${reason}`),
  ].join('\n');
}