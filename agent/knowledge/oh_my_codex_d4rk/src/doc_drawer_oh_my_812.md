ion starPromptStatePath(): string {
  return join(homedir(), '.omx', 'state', 'star-prompt.json');
}

export async function hasBeenPrompted(): Promise<boolean> {
  const path = starPromptStatePath();
  if (!existsSync(path)) return false;
  try {
    const content = await readFile(path, 'utf-8');
    const state = JSON.parse(content) as StarPromptState;
    return typeof state.prompted_at === 'string';
  } catch {
    return false;
  }
}

export async function markPrompted(): Promise<void> {
  const stateDir = join(homedir(), '.omx', 'state');
  await mkdir(stateDir, { recursive: true });
  await writeFile(
    starPromptStatePath(),
    JSON.stringify({ prompted_at: new Date().toISOString() }, null, 2),
  );
}