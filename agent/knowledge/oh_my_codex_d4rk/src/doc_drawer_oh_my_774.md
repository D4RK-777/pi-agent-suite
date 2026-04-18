h {
      continue;
    }

    if (!containsTomlKey(content, OBSOLETE_NATIVE_AGENT_FIELD)) continue;

    if (await ensureBackup(fullPath, true, backupContext, options)) {
      // backup created for pre-existing obsolete native agent config
    }
    if (!options.dryRun) {
      await rm(fullPath, { force: true });
    }
    if (options.verbose) {
      const prefix = options.dryRun
        ? "would remove stale obsolete native agent"
        : "removed stale obsolete native agent";
      console.log(`  ${prefix} ${file}`);
    }
    removed += 1;
  }

  return removed;
}