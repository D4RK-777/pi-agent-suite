ame = "editor-test"\ndescription = "Before edit"\ndeveloper_instructions = """before"""\n',
      );

      const editorScript = join(wd, 'editor.sh');
      await writeFile(
        editorScript,
        '#!/usr/bin/env bash\nprintf \'\\nmodel = "gpt-5.4"\\n\' >> "$1"\n',
      );
      await chmod(editorScript, 0o755);

      const editResult = runOmx(wd, ['agents', 'edit', 'editor-test', '--scope', 'project'], {
        HOME: home,
        CODEX_HOME: join(home, '.codex'),
        EDITOR: editorScript,
      });
      if (shouldSkipForSpawnPermissions(editResult.error)) return;

      assert.equal(editResult.status, 0, editResult.stderr || editResult.stdout);
      assert.match(await readFile(agentPath, 'utf-8'), /^model = "gpt-5\.4"$/m);