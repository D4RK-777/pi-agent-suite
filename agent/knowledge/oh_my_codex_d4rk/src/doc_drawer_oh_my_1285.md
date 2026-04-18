essBinaryName()), 0o755);
      await mkdir(join(wd, 'crates', 'omx-explore'), { recursive: true });
      await writeFile(join(wd, 'crates', 'omx-explore', 'Cargo.toml'), '[package]\nname="omx-explore-harness"\nversion="0.0.0"\n');

      const repoBuilt = repoBuiltExploreHarnessCommand(wd);
      assert.deepEqual(repoBuilt, { command: join(targetDir, packagedExploreHarnessBinaryName()), args: [] });

      const resolved = resolveExploreHarnessCommand(wd, {} as NodeJS.ProcessEnv);
      assert.deepEqual(resolved, { command: join(targetDir, packagedExploreHarnessBinaryName()), args: [] });
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });