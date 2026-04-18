ue });
      await writeFile(
        join(codexDir, 'config.toml'),
        `
[mcp_servers.non_omx]
command = "node"
`.trimStart(),
      );

      const res = runOmx(wd, ['doctor'], {
        HOME: home,
        CODEX_HOME: join(home, '.codex'),
      });
      if (shouldSkipForSpawnPermissions(res.error)) return;
      assert.equal(res.status, 0, res.stderr || res.stdout);
      assert.match(
        res.stdout,
        /Config: config\.toml exists but no OMX entries yet \(expected before first setup; run "omx setup --force" once\)/,
      );
      assert.match(
        res.stdout,
        /MCP Servers: 1 servers but no OMX servers yet \(expected before first setup; run "omx setup --force" once\)/,
      );
    } finally {
      await rm(wd, { recursive: true, force: true });
    }