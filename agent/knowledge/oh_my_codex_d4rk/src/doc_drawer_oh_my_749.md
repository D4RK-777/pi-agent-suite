else {
      const result = await syncManagedAgentsContent(
        rewritten,
        agentsMdDst,
        summary.agentsMd,
        backupContext,
        {
          agentsOverwritePrompt: options.agentsOverwritePrompt,
          dryRun,
          force,
          verbose,
        },
      );

      if (result === "updated") {
        console.log(
          resolvedScope.scope === "project"
            ? "  Generated AGENTS.md in project root."
            : `  Generated AGENTS.md in ${scopeDirs.codexHomeDir}.`,
        );
      } else if (result === "unchanged") {
        console.log(
          resolvedScope.scope === "project"
            ? "  AGENTS.md already up to date in project root."
            : `  AGENTS.md already up to date in ${scopeDirs.codexHomeDir}.`,
        );