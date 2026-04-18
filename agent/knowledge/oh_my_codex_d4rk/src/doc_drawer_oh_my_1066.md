s'), 'export const value = 1;\n');
      await writeFile(join(wd, 'docs', 'guide.md'), '# guide\n');
      await writeFile(join(wd, 'package.json'), '{"name":"fixture"}\n');

      await withCwd(wd, async () => {
        await agentsInit();
      });

      const rootAgents = await readFile(join(wd, 'AGENTS.md'), 'utf-8');
      const srcAgents = await readFile(join(wd, 'src', 'AGENTS.md'), 'utf-8');
      const docsAgents = await readFile(join(wd, 'docs', 'AGENTS.md'), 'utf-8');