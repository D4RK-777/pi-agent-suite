String('utf-8').trim()
        : '';
    throw contractError(stderr || MISSION_DIR_GIT_ERROR);
  }
}

export function slugifyMissionName(value: string): string {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 48) || 'mission';
}

function ensurePathInside(parentPath: string, childPath: string): void {
  const rel = relative(parentPath, childPath);
  if (rel === '' || (!rel.startsWith('..') && rel !== '..')) return;
  throw contractError(MISSION_DIR_GIT_ERROR);
}