log(
    "- Avoids rewriting project-root AGENTS.md while an active omx session is running.\n",
  );

  console.log("Summary:");
  console.log(
    `  updated=${summary.updated}, unchanged=${summary.unchanged}, backed_up=${summary.backedUp}, skipped=${summary.skipped}`,
  );
}

export async function agentsInitCommand(args: string[]): Promise<void> {
  if (args.includes("--help") || args.includes("-h")) {
    console.log(AGENTS_INIT_USAGE);
    return;
  }

  const allowedFlags = new Set(["--dry-run", "--force", "--verbose"]);
  for (const arg of args) {
    if (!arg.startsWith("-")) continue;
    if (!allowedFlags.has(arg)) {
      throw new Error(
        `Unknown agents-init option: ${arg}\n${AGENTS_INIT_USAGE}`,
      );
    }
  }