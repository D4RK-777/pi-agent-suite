const thirdContract = await materializeAutoresearchMissionToWorktree(contract, thirdWorktreePath);
      const thirdRuntime = await prepareAutoresearchRuntime(thirdContract, repo, thirdWorktreePath, { runTag: '20260314T072000Z' });

      manifest = await loadAutoresearchRunManifest(repo, thirdRuntime.runId);
      await rm(thirdRuntime.candidateFile, { force: true });
      assert.equal(await processAutoresearchCandidate(thirdContract, manifest, repo), 'error');
      failedManifest = await loadAutoresearchRunManifest(repo, thirdRuntime.runId);
      assert.equal(failedManifest.status, 'failed');
      assert.match(failedManifest.stop_reason || '', /autoresearch_candidate_missing/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });