) throw new Error('[native-assets] package.json is missing version');
  return pkg.version.trim();
}

function repositoryHttpBase(repository: { url?: string } | string | undefined): string | undefined {
  const raw = typeof repository === 'string' ? repository : repository?.url;
  if (!raw?.trim()) return undefined;
  const trimmed = raw.trim().replace(/^git\+/, '').replace(/\.git$/, '');
  if (trimmed.startsWith('https://github.com/')) return trimmed;
  if (trimmed.startsWith('http://github.com/')) return trimmed.replace(/^http:/, 'https:');
  return undefined;
}