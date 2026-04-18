eParentDir(filePath);
  await writeFile(filePath, `${JSON.stringify(value, null, 2)}\n`, 'utf-8');
}

async function readJsonFile<T>(filePath: string): Promise<T> {
  return JSON.parse(await readFile(filePath, 'utf-8')) as T;
}

async function readActiveRunState(projectRoot: string): Promise<AutoresearchActiveRunState | null> {
  const file = activeRunStateFile(projectRoot);
  if (!existsSync(file)) return null;
  return readJsonFile<AutoresearchActiveRunState>(file);
}

async function writeActiveRunState(projectRoot: string, value: AutoresearchActiveRunState): Promise<void> {
  await writeJsonFile(activeRunStateFile(projectRoot), value);
}