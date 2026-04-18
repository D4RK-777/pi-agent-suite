missionDir = join(repo, 'missions', 'existing');
      await mkdir(missionDir, { recursive: true });

      await assert.rejects(
        () => initAutoresearchMission({
          topic: 'duplicate',
          evaluatorCommand: 'echo ok',
          keepPolicy: 'pass_only',
          slug: 'existing',
          repoRoot: repo,
        }),
        /already exists/,
      );
    } finally {
      await rm(repo, { recursive: true, force: true });
    }
  });
});