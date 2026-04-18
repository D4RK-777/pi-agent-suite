ow new Error(
        `Unknown agents-init option: ${arg}\n${AGENTS_INIT_USAGE}`,
      );
    }
  }

  const positionals = args.filter((arg) => !arg.startsWith("-"));
  if (positionals.length > 1) {
    throw new Error(
      `agents-init accepts at most one path argument.\n${AGENTS_INIT_USAGE}`,
    );
  }

  await agentsInit({
    targetPath: positionals[0],
    dryRun: args.includes("--dry-run"),
    force: args.includes("--force"),
    verbose: args.includes("--verbose"),
  });
}