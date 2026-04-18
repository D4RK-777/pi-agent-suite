d = LEGACY_SCOPE_MIGRATION_SYNC[parsed.scope];
      if (migrated) persisted.scope = migrated;
    }
    return Object.keys(persisted).length > 0 ? persisted : undefined;
  } catch (err) {
    process.stderr.write(`[cli/index] operation failed: ${err}\n`);
    // Ignore malformed persisted scope and use defaults.
  }
  return undefined;
}

export function resolveCodexHomeForLaunch(
  cwd: string,
  env: NodeJS.ProcessEnv = process.env,
): string | undefined {
  if (env.CODEX_HOME && env.CODEX_HOME.trim() !== "") return env.CODEX_HOME;
  const persistedScope = readPersistedSetupScope(cwd);
  if (persistedScope === "project") {
    return join(cwd, ".codex");
  }
  return undefined;
}