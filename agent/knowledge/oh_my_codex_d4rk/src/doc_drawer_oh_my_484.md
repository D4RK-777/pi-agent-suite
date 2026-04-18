sifyLongOutputShellCommand(argv) ? 'long-output' : 'shell-native',
    };
  }

  return undefined;
}

async function runExploreViaSparkShell(route: ExploreSparkShellRoute, env: NodeJS.ProcessEnv = process.env): Promise<void> {
  const binaryPath = await resolveSparkShellBinaryPathWithHydration({ cwd: process.cwd(), env });
  const result = runSparkShellBinary(binaryPath, route.argv, { cwd: process.cwd(), env });

  if (result.error) {
    const errno = result.error as NodeJS.ErrnoException;
    throw new Error(`[explore] failed to launch sparkshell backend: ${errno.message}`);
  }

  if (isSparkShellNativeCompatibilityFailure(result)) {
    throw new Error('[explore] sparkshell backend is incompatible with this Linux runtime (missing GLIBC symbols)');
  }