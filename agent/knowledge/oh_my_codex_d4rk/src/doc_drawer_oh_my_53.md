ual(skipped, 0);
    } finally {
      await rm(root, { recursive: true, force: true });
    }
  });

  it("keeps standard agents off a custom gpt-5.2 root model", async () => {
    const root = await mkdtemp(join(tmpdir(), "omx-native-config-root-model-"));
    const codexHome = join(root, ".codex");
    const promptsDir = join(root, "prompts");
    const outDir = join(codexHome, "agents");
    const previousCodexHome = process.env.CODEX_HOME;