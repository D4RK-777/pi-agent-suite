eFile(join(crateDir, 'Cargo.toml'), '[package]\nname = "omx-explore-harness"\nversion = "0.0.0"\n');

      const resolved = resolveExploreHarnessCommand(wd, {} as NodeJS.ProcessEnv);
      assert.equal(resolved.command, 'cargo');
      assert.ok(resolved.args.includes('--manifest-path'));
      assert.ok(resolved.args.includes(join(wd, 'crates', 'omx-explore', 'Cargo.toml')));
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });