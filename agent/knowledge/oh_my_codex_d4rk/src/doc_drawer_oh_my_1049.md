ot, ".omx", "setup-scope.json");
    const hudConfig = join(projectRoot, ".omx", "hud-config.json");
    for (const f of [scopeFile, hudConfig]) {
      if (existsSync(f)) {
        if (!dryRun) await rm(f, { force: true });
        if (verbose)
          console.log(
            `  ${dryRun ? "Would remove" : "Removed"} ${basename(f)}`,
          );
      }
    }
  }
  console.log();

  printSummary(summary, dryRun);

  if (!dryRun) {
    console.log(
      '\noh-my-codex has been uninstalled. Run "omx setup" to reinstall.',
    );
  } else {
    console.log("\nRun without --dry-run to apply changes.");
  }
}