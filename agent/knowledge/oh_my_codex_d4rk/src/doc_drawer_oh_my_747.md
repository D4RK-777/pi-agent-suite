const existing = await readFile(agentsMdDst, "utf-8");
      changed = existing !== rewritten;
      if (isOmxGeneratedAgentsMd(existing)) {
        managedRefreshContent = upsertAgentsModelTable(
          existing,
          modelTableContext,
        );
        canApplyManagedModelRefresh = managedRefreshContent !== existing;
      }
    }

    if (
      resolvedScope.scope === "project" &&
      sessionIsActive &&
      agentsMdExists &&
      changed
    ) {
      summary.agentsMd.skipped += 1;
      console.log(
        "  WARNING: Active omx session detected (pid " +
          activeSession?.pid +
          ").",
      );
      console.log(
        "  Skipping AGENTS.md overwrite to avoid corrupting runtime overlay.",
      );