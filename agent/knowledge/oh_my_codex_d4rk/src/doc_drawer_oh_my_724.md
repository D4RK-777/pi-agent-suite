rsisted.scope = parsed.scope;
      }
      // Migrate legacy scope values (project-local → project)
      const migrated = LEGACY_SCOPE_MIGRATION[parsed.scope];
      if (migrated) {
        console.warn(
          `[omx] Migrating persisted setup scope "${parsed.scope}" → "${migrated}" ` +
            `(see issue #243: simplified to user/project).`,
        );
        persisted.scope = migrated;
      }
    }
    return Object.keys(persisted).length > 0 ? persisted : undefined;
  } catch {
    // ignore invalid persisted scope and fall back to prompt/default
  }
  return undefined;
}