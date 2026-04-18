nd(commandText: string): string {
  return Buffer.from(commandText, "utf16le").toString("base64");
}

function isCodexVersionRequest(args: string[]): boolean {
  return args.some((arg) => CODEX_VERSION_FLAGS.has(arg));
}

export function buildWindowsPromptCommand(
  command: string,
  args: string[],
): string {
  const invocation = [
    "&",
    quotePowerShellArg(command),
    ...args.map(quotePowerShellArg),
  ].join(" ");
  const wrappedCommand = [
    "$ErrorActionPreference = 'Stop'",
    `& { ${invocation} }`,
  ].join("; ");
  return `powershell.exe -NoLogo -NoExit -EncodedCommand ${encodePowerShellCommand(wrappedCommand)}`;
}