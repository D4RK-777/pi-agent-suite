return answer === '' || answer === 'y' || answer === 'yes';
  } finally {
    rl.close();
  }
}

interface UpdateDependencies {
  askYesNo: typeof askYesNo;
  fetchLatestVersion: typeof fetchLatestVersion;
  getCurrentVersion: typeof getCurrentVersion;
  runGlobalUpdate: typeof runGlobalUpdate;
  setup: typeof setup;
}

const defaultUpdateDependencies: UpdateDependencies = {
  askYesNo,
  fetchLatestVersion,
  getCurrentVersion,
  runGlobalUpdate,
  setup,
};

export async function maybeCheckAndPromptUpdate(
  cwd: string,
  dependencies: Partial<UpdateDependencies> = {},
): Promise<void> {
  const updateDependencies = { ...defaultUpdateDependencies, ...dependencies };
  if (process.env.OMX_AUTO_UPDATE === '0') return;
  if (!process.stdin.isTTY || !process.stdout.isTTY) return;