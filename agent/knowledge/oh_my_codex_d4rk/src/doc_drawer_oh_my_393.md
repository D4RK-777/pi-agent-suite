while (true) {
      runAutoresearchTurn(runtime.worktreePath, runtime.instructionsFile, codexArgs);

      const contract = await loadAutoresearchMissionContract(missionDir);
      const { run_id: runId } = JSON.parse(readFileSync(runtime.manifestFile, 'utf-8')) as { run_id: string };
      const manifest = await loadAutoresearchRunManifest(runtime.repoRoot, runId);
      const decision = await processAutoresearchCandidate(contract, manifest, runtime.repoRoot);
      if (decision === 'abort' || decision === 'error') {
        return;
      }
      if (decision === 'noop') {
        const trailingNoops = await countTrailingAutoresearchNoops(manifest.ledger_file);
        if (trailingNoops >= AUTORESEARCH_MAX_CONSECUTIVE_NOOPS) {