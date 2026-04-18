re] sparkshell backend unavailable (${message}). Falling back to the explore harness.\n`);
    }
  }

  const packageRoot = getPackageRoot();
  const harness = await resolveExploreHarnessCommandWithHydration(packageRoot, process.env);
  const harnessArgs = [...harness.args, ...buildExploreHarnessArgs(prompt, process.cwd(), process.env, packageRoot)];

  const { result } = spawnPlatformCommandSync(harness.command, harnessArgs, {
    cwd: process.cwd(),
    env: process.env,
    encoding: 'utf-8',
    stdio: ['ignore', 'pipe', 'pipe'],
  });

  if (result.stdout && result.stdout.length > 0) process.stdout.write(result.stdout);
  if (result.stderr && result.stderr.length > 0) process.stderr.write(result.stderr);