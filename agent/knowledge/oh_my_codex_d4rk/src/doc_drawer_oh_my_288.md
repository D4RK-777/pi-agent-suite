e(destinationPath, content);
  }
  summary.updated += 1;
  return { action: "updated", backedUp };
}

export async function agentsInit(
  options: AgentsInitOptions = {},
): Promise<void> {
  const dryRun = options.dryRun === true;
  const force = options.force === true;
  const verbose = options.verbose === true;
  const cwd = process.cwd();
  const requestedTarget = options.targetPath ?? ".";
  const targetDir = resolve(cwd, requestedTarget);
  const relativeTarget = relative(cwd, targetDir);

  if (relativeTarget.startsWith("..")) {
    throw new Error(
      `agents-init target must stay inside the current working directory: ${requestedTarget}`,
    );
  }