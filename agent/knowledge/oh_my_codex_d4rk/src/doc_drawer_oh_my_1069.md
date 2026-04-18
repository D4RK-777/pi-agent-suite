);

      await withCwd(wd, async () => {
        await agentsInit({ targetPath: 'src' });
      });

      const agentsPath = join(wd, 'src', 'AGENTS.md');
      const initial = await readFile(agentsPath, 'utf-8');
      const customized = initial.replace(
        '- Add subtree-specific constraints, ownership notes, and test commands here.',
        '- Preserve this custom manual note.',
      );
      await writeFile(agentsPath, customized);
      await writeFile(join(wd, 'src', 'new-file.ts'), 'export const newer = true;\n');

      await withCwd(wd, async () => {
        await agentsInit({ targetPath: 'src' });
      });