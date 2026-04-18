"existing unmanaged AGENTS.md (re-run with --force to adopt it)",
      backedUp: false,
    };
  }

  const backedUp = await ensureBackup(
    destinationPath,
    backupRoot,
    options.dryRun,
  );
  if (backedUp) summary.backedUp += 1;

  if (!options.dryRun) {
    await mkdir(dirname(destinationPath), { recursive: true });
    await writeFile(destinationPath, content);
  }
  summary.updated += 1;
  return { action: "updated", backedUp };
}