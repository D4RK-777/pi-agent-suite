mResultPath(resultPath: string): string {
  return dirname(dirname(dirname(dirname(resultPath))));
}

function isUsableAbsolutePath(path: string | undefined): path is string {
  return typeof path === 'string' && path.startsWith('/') && !path.includes('${');
}

async function readPersistedResult(resultPath: string): Promise<AutoresearchDeepInterviewResult> {
  const raw = await readFile(resultPath, 'utf-8');
  const parsed = JSON.parse(raw) as Partial<PersistedAutoresearchDeepInterviewResultV1>;
  if (parsed.kind !== AUTORESEARCH_DEEP_INTERVIEW_RESULT_KIND) {
    throw new Error(`Unsupported autoresearch deep-interview result payload: ${resultPath}`);
  }
  if (!parsed.compileTarget) {
    throw new Error(`Missing compileTarget in ${resultPath}`);
  }