rgv,
      reason: classifyLongOutputShellCommand(argv) ? 'long-output' : 'shell-native',
    };
  }

  const shellNativeShape = explicitShellPrefix || argv.slice(1).some((arg) => (
    arg.startsWith('-')
    || arg.includes('/')
    || arg === '.'
    || arg.includes('*')
  ));

  if (
    explicitShellPrefix
    && shellNativeShape
    && ['find', 'ls', 'rg', 'grep'].includes(command)
    && argv.slice(1).every((arg) => !arg.startsWith('/') && !arg.startsWith('..'))
  ) {
    return {
      argv,
      reason: classifyLongOutputShellCommand(argv) ? 'long-output' : 'shell-native',
    };
  }

  return undefined;
}