mkdir(projectAgentsDir, { recursive: true });
      await mkdir(userAgentsDir, { recursive: true });

      await writeFile(
        join(projectAgentsDir, 'planner.toml'),
        'name = "planner"\ndescription = "Project planner"\nmodel = "gpt-5.4"\ndeveloper_instructions = """plan"""\n',
      );
      await writeFile(
        join(userAgentsDir, 'reviewer.toml'),
        'name = "reviewer"\ndescription = "User reviewer"\ndeveloper_instructions = """review"""\n',
      );

      const result = runOmx(wd, ['agents', 'list'], {
        HOME: home,
        CODEX_HOME: join(home, '.codex'),
      });
      if (shouldSkipForSpawnPermissions(result.error)) return;