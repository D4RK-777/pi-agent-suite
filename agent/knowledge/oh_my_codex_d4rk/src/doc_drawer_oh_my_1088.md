ame = "non-interactive"\ndescription = "Remove me"\ndeveloper_instructions = """noop"""\n',
      );

      const result = runOmx(wd, ['agents', 'remove', 'non-interactive', '--scope', 'project'], {
        HOME: home,
        CODEX_HOME: join(home, '.codex'),
      });
      if (shouldSkipForSpawnPermissions(result.error)) return;

      assert.notEqual(result.status, 0, 'expected non-zero exit for non-interactive remove');
      assert.equal(existsSync(agentPath), true, 'agent file should remain when remove aborts');
      assert.match(
        result.stderr,
        /remove requires an interactive terminal; rerun with --force in non-interactive environments/i,
      );
    } finally {
      await rm(wd, { recursive: true, force: true });
    }
  });
});