mpt, {
      env: { OMX_DEFAULT_STANDARD_MODEL: "gpt-5.4-mini-tuned" } as NodeJS.ProcessEnv,
    });

    assert.match(exactMiniToml, /exact gpt-5\.4-mini model/);
    assert.match(exactMiniToml, /strict execution order: inspect -> plan -> act -> verify/);
    assert.match(exactMiniToml, /resolved_model: gpt-5\.4-mini/);
    assert.doesNotMatch(frontierToml, /exact gpt-5\.4-mini model/);
    assert.doesNotMatch(tunedToml, /exact gpt-5\.4-mini model/);
  });

  it("installs only agents with prompt files and skips existing files without force", async () => {
    const root = await mkdtemp(join(tmpdir(), "omx-native-config-"));
    const promptsDir = join(root, "prompts");
    const outDir = join(root, "agents-out");