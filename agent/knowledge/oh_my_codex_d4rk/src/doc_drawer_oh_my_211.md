ts_file, runtime.resultsFile);
      assert.equal(state?.baseline_commit, manifest.baseline_commit);

      const instructions = await readFile(runtime.instructionsFile, 'utf-8');
      assert.match(instructions, /Last kept score:\s+1/i);
      assert.match(instructions, /previous_iteration_outcome/i);
      assert.match(instructions, /baseline established/i);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });
});