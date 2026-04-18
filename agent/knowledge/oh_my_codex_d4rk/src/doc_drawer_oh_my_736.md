log(`  mkdir ${dir}`);
  }
  await persistSetupScope(projectRoot, resolvedScope.scope, {
    dryRun,
    verbose,
  });
  console.log("  Done.\n");

  if (resolvedScope.scope === "project") {
    const gitignoreResult = await ensureProjectOmxGitignore(
      projectRoot,
      backupContext,
      { dryRun, verbose },
    );
    if (gitignoreResult === "created") {
      console.log(
        "  Created .gitignore with .omx/ so local OMX runtime state stays out of source control.\n",
      );
    } else if (gitignoreResult === "updated") {
      console.log(
        "  Added .omx/ to .gitignore so local OMX runtime state stays out of source control.\n",
      );
    }
  }

  const catalogCounts = getCatalogHeadlineCounts();
  const summary = createEmptyRunSummary();