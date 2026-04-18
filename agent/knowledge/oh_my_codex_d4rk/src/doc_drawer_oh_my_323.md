er === 'number' && Number.isFinite(signalNumber)) {
    return 128 + signalNumber;
  }
  return 1;
}

export async function askCommand(args: string[]): Promise<void> {
  if (args[0] === '--help' || args[0] === '-h') {
    console.log(ASK_USAGE);
    return;
  }

  const parsed = parseAskArgs(args);
  const packageRoot = getPackageRoot();
  const advisorScriptPath = resolveAskAdvisorScriptPath(packageRoot);
  const promptsDir = resolveAskPromptsDir(process.cwd(), process.env);

  if (!existsSync(advisorScriptPath)) {
    throw new Error(`[ask] advisor script not found: ${advisorScriptPath}`);
  }