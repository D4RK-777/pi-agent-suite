p-scope.json');
  if (!existsSync(scopePath)) {
    return { scope: 'user', source: 'default' };
  }

  try {
    const raw = await readFile(scopePath, 'utf-8');
    const parsed = JSON.parse(raw) as Partial<{ scope: string }>;
    if (typeof parsed.scope === 'string') {
      if (parsed.scope === 'user' || parsed.scope === 'project') {
        return { scope: parsed.scope, source: 'persisted' };
      }
      const migrated = LEGACY_SCOPE_MIGRATION[parsed.scope];
      if (migrated) {
        return { scope: migrated, source: 'persisted' };
      }
    }
  } catch {
    // ignore invalid persisted scope and fall back to default
  }

  return { scope: 'user', source: 'default' };
}