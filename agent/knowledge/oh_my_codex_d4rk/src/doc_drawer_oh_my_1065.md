19]);
    return Number.isFinite(ticks) ? ticks : undefined;
  } catch {
    return undefined;
  }
}

describe('omx agents-init', () => {
  it('creates a managed root AGENTS.md plus direct-child AGENTS.md files while skipping ignored directories', async () => {
    const wd = await mkdtemp(join(tmpdir(), 'omx-agents-init-'));
    try {
      await mkdir(join(wd, 'src'), { recursive: true });
      await mkdir(join(wd, 'docs'), { recursive: true });
      await mkdir(join(wd, 'node_modules', 'dep'), { recursive: true });
      await mkdir(join(wd, 'dist'), { recursive: true });
      await writeFile(join(wd, 'src', 'index.ts'), 'export const value = 1;\n');
      await writeFile(join(wd, 'docs', 'guide.md'), '# guide\n');