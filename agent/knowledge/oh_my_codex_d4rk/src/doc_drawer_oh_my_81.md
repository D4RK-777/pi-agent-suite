un.log', 'node_modules', '.omx/'];

function nowIso(): string {
  return new Date().toISOString();
}

export function buildAutoresearchRunTag(date = new Date()): string {
  const iso = date.toISOString();
  return iso
    .replace(/[-:]/g, '')
    .replace(/\.\d{3}Z$/, 'Z')
    .replace('T', 'T');
}

function buildRunId(missionSlug: string, runTag: string): string {
  return `${missionSlug}-${runTag.toLowerCase()}`;
}

function activeRunStateFile(projectRoot: string): string {
  return join(projectRoot, '.omx', 'state', 'autoresearch-state.json');
}

function trimContent(value: string, max = 4000): string {
  const trimmed = value.trim();
  return trimmed.length <= max ? trimmed : `${trimmed.slice(0, max)}\n...`;
}