mber.isFinite(parsed) || parsed < MIN_SPARKSHELL_TAIL_LINES || parsed > MAX_SPARKSHELL_TAIL_LINES) {
        throw new Error(`Usage: omx team status <team-name> [--json] [--tail-lines <${MIN_SPARKSHELL_TAIL_LINES}-${MAX_SPARKSHELL_TAIL_LINES}>]`);
      }
      return parsed;
    }
    if (token.startsWith('--tail-lines=')) {
      const parsed = Number.parseInt(token.slice('--tail-lines='.length), 10);
      if (!Number.isFinite(parsed) || parsed < MIN_SPARKSHELL_TAIL_LINES || parsed > MAX_SPARKSHELL_TAIL_LINES) {
        throw new Error(`Usage: omx team status <team-name> [--json] [--tail-lines <${MIN_SPARKSHELL_TAIL_LINES}-${MAX_SPARKSHELL_TAIL_LINES}>]`);
      }
      return parsed;
    }
  }
  return DEFAULT_SPARKSHELL_TAIL_LINES;
}