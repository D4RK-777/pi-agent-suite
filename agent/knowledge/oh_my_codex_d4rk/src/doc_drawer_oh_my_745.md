sage}`);
    console.log("  Run `npm run build` and then re-run `omx setup`.");
  }
  console.log();

  // Step 6: Generate AGENTS.md
  console.log("[6/8] Generating AGENTS.md...");
  const agentsMdSrc = join(pkgRoot, "templates", "AGENTS.md");
  const agentsMdDst =
    resolvedScope.scope === "project"
      ? join(projectRoot, "AGENTS.md")
      : join(scopeDirs.codexHomeDir, "AGENTS.md");
  const agentsMdExists = existsSync(agentsMdDst);

  // Guard: refuse to overwrite project-root AGENTS.md during active session
  const activeSession =
    resolvedScope.scope === "project"
      ? await readSessionState(projectRoot)
      : null;
  const sessionIsActive = activeSession && !isSessionStale(activeSession);