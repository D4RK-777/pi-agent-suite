unts.skills}).\n`,
      );
    } else {
      console.log("  Skill refresh complete.\n");
    }
  }

  // Step 4: Install native agent configs
  console.log("[4/8] Installing native agent configs...");
  {
    summary.nativeAgents = await refreshNativeAgentConfigs(
      pkgRoot,
      scopeDirs.nativeAgentsDir,
      backupContext,
      {
        force,
        dryRun,
        verbose,
      },
    );
    console.log(
      `  Native agent refresh complete (${scopeDirs.nativeAgentsDir}).\n`,
    );
  }