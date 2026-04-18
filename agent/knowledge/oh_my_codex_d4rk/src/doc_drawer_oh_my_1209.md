true });

      await writeFile(
        join(codexDir, 'config.toml'),
        `
model = "gpt-5.4"

[tui]
status_line = ["model-with-reasoning"]

[tui]
theme = "base16-ocean-light"
`.trimStart(),
      );

      const res = runOmx(wd, ['doctor'], {
        HOME: home,
        CODEX_HOME: codexDir,
      });

      if (shouldSkipForSpawnPermissions(res.error)) return;

      assert.equal(res.status, 0, res.stderr || res.stdout);
      assert.match(
        res.stdout,
        /\[XX\] Config: invalid config\.toml \(possible duplicate TOML table such as \[tui\]\)/,
      );
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });
});