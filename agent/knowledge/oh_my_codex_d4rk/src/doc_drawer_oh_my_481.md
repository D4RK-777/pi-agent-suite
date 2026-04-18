^--(?:stat|name-only|name-status|numstat|shortstat)$/.test(arg));
  }
  if (subcommand === 'show') {
    return args.some((arg) => /^--(?:stat|summary|name-only|name-status)$/.test(arg));
  }
  return true;
}

function classifyLongOutputShellCommand(args: readonly string[]): boolean {
  const [command, subcommand] = args;
  if (command === 'git') {
    return ['log', 'diff', 'status', 'show'].includes((subcommand || '').toLowerCase());
  }
  return ['find', 'ls', 'rg', 'grep'].includes(command);
}