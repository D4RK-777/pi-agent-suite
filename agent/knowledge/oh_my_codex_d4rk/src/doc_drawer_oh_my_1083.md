h = join(wd, '.codex', 'agents', 'my-helper.toml');
      assert.equal(existsSync(agentPath), true);

      const content = await readFile(agentPath, 'utf-8');
      assert.match(content, /^name = "my-helper"$/m);
      assert.match(content, /^description = "TODO: describe this agent's purpose"$/m);
      assert.match(content, /^developer_instructions = """$/m);
      assert.match(content, /^# model = "gpt-5\.4"$/m);
      assert.match(content, /^# model_reasoning_effort = "medium"$/m);
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });