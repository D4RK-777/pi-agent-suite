(${PROJECT_OMX_GITIGNORE_ENTRY})`,
    );
  }

  return destinationExists ? "updated" : "created";
}

async function persistSetupScope(
  projectRoot: string,
  scope: SetupScope,
  options: Pick<SetupOptions, "dryRun" | "verbose">,
): Promise<void> {
  const scopePath = getScopeFilePath(projectRoot);
  if (options.dryRun) {
    if (options.verbose) console.log(`  dry-run: skip persisting ${scopePath}`);
    return;
  }
  await mkdir(dirname(scopePath), { recursive: true });
  const payload: PersistedSetupScope = { scope };
  await writeFile(scopePath, JSON.stringify(payload, null, 2) + "\n");
  if (options.verbose) console.log(`  Wrote ${scopePath}`);
}