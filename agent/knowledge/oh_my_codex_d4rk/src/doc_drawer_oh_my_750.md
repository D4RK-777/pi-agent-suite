ject root."
            : `  AGENTS.md already up to date in ${scopeDirs.codexHomeDir}.`,
        );
      } else if (agentsMdExists) {
        console.log(
          `  Skipped AGENTS.md overwrite for ${agentsMdDst}. Re-run interactively to confirm or use --force.`,
        );
      }
    }
    if (resolvedScope.scope === "user") {
      console.log("  User scope leaves project AGENTS.md unchanged.");
    }
  } else {
    summary.agentsMd.skipped += 1;
    console.log("  AGENTS.md template not found, skipping.");
  }
  console.log();

  // Step 7: Set up notify hook
  console.log("[7/8] Configuring notification hook...");
  await setupNotifyHook(pkgRoot, { dryRun, verbose });
  console.log("  Done.\n");