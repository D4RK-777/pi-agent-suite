,
      hudCmd,
    ],
    { encoding: "utf-8" },
  );
  return parsePaneIdFromTmuxOutput(output);
}

function killTmuxPane(paneId: string): void {
  if (!paneId.startsWith("%")) return;
  try {
    execFileSync("tmux", ["kill-pane", "-t", paneId], { stdio: "ignore" });
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Pane may already be gone; ignore.
  }
}

export function buildTmuxShellCommand(command: string, args: string[]): string {
  return [quoteShellArg(command), ...args.map(quoteShellArg)].join(" ");
}

function encodePowerShellCommand(commandText: string): string {
  return Buffer.from(commandText, "utf16le").toString("base64");
}