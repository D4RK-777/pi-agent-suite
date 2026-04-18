PassValue(value: boolean | undefined): string {
  return value === undefined ? '' : String(value);
}

function resultScoreValue(value: number | undefined | null): string {
  return typeof value === 'number' ? String(value) : '';
}

async function initializeAutoresearchResultsFile(resultsFile: string): Promise<void> {
  if (existsSync(resultsFile)) return;
  await ensureParentDir(resultsFile);
  await writeFile(resultsFile, AUTORESEARCH_RESULTS_HEADER, 'utf-8');
}