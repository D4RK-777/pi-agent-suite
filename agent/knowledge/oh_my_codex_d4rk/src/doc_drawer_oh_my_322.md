er: provider as AskProvider,
    prompt,
    ...(agentPromptRole ? { agentPromptRole } : {}),
  };
}

export function resolveAskAdvisorScriptPath(
  packageRoot = getPackageRoot(),
  env: NodeJS.ProcessEnv = process.env,
): string {
  const override = env[ASK_ADVISOR_SCRIPT_ENV]?.trim();
  if (override) {
    return isAbsolute(override) ? override : join(packageRoot, override);
  }
  return join(packageRoot, 'dist', 'scripts', 'run-provider-advisor.js');
}

function resolveSignalExitCode(signal: NodeJS.Signals | null): number {
  if (!signal) return 1;
  const signalNumber = osConstants.signals[signal];
  if (typeof signalNumber === 'number' && Number.isFinite(signalNumber)) {
    return 128 + signalNumber;
  }
  return 1;
}