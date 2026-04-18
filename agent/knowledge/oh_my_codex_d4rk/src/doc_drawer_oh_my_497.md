BIN to a prebuilt harness binary.');
  }

  return resolveExploreHarnessCommand(packageRoot, env);
}

export function buildExploreHarnessArgs(
  prompt: string,
  cwd: string,
  env: NodeJS.ProcessEnv = process.env,
  packageRoot = getPackageRoot(),
): string[] {
  const sparkModel = env[EXPLORE_SPARK_MODEL_ENV]?.trim() || getSparkDefaultModel();
  return [
    '--cwd', cwd,
    '--prompt', prompt,
    '--prompt-file', join(packageRoot, 'prompts', 'explore-harness.md'),
    '--model-spark', sparkModel,
    '--model-fallback', getMainDefaultModel(),
  ];
}