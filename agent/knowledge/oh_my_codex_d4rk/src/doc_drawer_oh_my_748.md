console.log(
        "  Skipping AGENTS.md overwrite to avoid corrupting runtime overlay.",
      );
      console.log("  Stop the active session first, then re-run setup.");
    } else if (canApplyManagedModelRefresh) {
      await syncManagedContent(
        managedRefreshContent,
        agentsMdDst,
        summary.agentsMd,
        backupContext,
        { dryRun, verbose },
        `AGENTS model table ${agentsMdDst}`,
      );
      console.log(
        resolvedScope.scope === "project"
          ? "  Refreshed AGENTS.md model capability table in project root."
          : `  Refreshed AGENTS.md model capability table in ${scopeDirs.codexHomeDir}.`,
      );
    } else {
      const result = await syncManagedAgentsContent(
        rewritten,
        agentsMdDst,