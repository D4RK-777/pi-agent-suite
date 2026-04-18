NTS.md'), 'utf-8');
      const docsAgents = await readFile(join(wd, 'docs', 'AGENTS.md'), 'utf-8');

      assert.match(rootAgents, /OMX:AGENTS-INIT:MANAGED/);
      assert.match(rootAgents, /<!-- AUTONOMY DIRECTIVE — DO NOT REMOVE -->/);
      assert.match(rootAgents, /<!-- END AUTONOMY DIRECTIVE -->\n\n# oh-my-codex - Intelligent Multi-Agent Orchestration/);
      assert.match(rootAgents, /# oh-my-codex - Intelligent Multi-Agent Orchestration/);
      assert.match(rootAgents, /\.\/\.codex/);
      assert.match(srcAgents, /<!-- Parent: ..\/AGENTS\.md -->/);
      assert.match(srcAgents, /`index\.ts`/);
      assert.match(docsAgents, /`guide\.md`/);
      assert.equal(existsSync(join(wd, 'node_modules', 'AGENTS.md')), false);