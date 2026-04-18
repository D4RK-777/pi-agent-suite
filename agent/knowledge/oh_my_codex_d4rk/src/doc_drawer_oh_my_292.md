yRisk
        ? "active omx session detected for project root AGENTS.md"
        : undefined,
    );

    if (verbose || decision.action !== "unchanged") {
      const label =
        decision.action === "updated"
          ? dryRun
            ? "would update"
            : "updated"
          : decision.action === "unchanged"
            ? "unchanged"
            : "skipped";
      const reason = decision.reason ? ` (${decision.reason})` : "";
      console.log(`  ${label} ${relativeDir}/AGENTS.md${reason}`);
    }
  }