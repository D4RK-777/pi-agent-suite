ntry.decision, entry.description]),
        [
          ['baseline', 'initial baseline evaluation'],
          ['keep', 'improved score'],
          ['discard', 'worse score'],
        ],
      );

      const instructions = await readFile(runtime.instructionsFile, 'utf-8');
      assert.match(instructions, /"previous_iteration_outcome": "discard:score did not improve"/);
      assert.match(instructions, /"decision": "keep"/);
      assert.match(instructions, /"decision": "discard"/);
      assert.equal(finalManifest.last_kept_commit, improvedCommit);
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });
});