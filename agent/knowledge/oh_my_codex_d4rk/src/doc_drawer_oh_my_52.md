utDir, "executor.toml")), true);
      assert.equal(existsSync(join(outDir, "planner.toml")), true);

      const executorToml = await readFile(
        join(outDir, "executor.toml"),
        "utf8",
      );
      assert.match(executorToml, /model = "gpt-5\.4"/);
      assert.match(executorToml, /model_reasoning_effort = "high"/);

      const skipped = await installNativeAgentConfigs(root, {
        agentsDir: outDir,
      });
      assert.equal(skipped, 0);
    } finally {
      await rm(root, { recursive: true, force: true });
    }
  });