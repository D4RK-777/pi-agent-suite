ents/skills after confirming ${overlap.canonicalDir} is the version you want Codex to load.`,
  };
}

function logCategorySummary(name: string, summary: SetupCategorySummary): void {
  console.log(
    `  ${name}: updated=${summary.updated}, unchanged=${summary.unchanged}, ` +
      `backed_up=${summary.backedUp}, skipped=${summary.skipped}, removed=${summary.removed}`,
  );
}

function isSetupScope(value: string): value is SetupScope {
  return SETUP_SCOPES.includes(value as SetupScope);
}
function getScopeFilePath(projectRoot: string): string {
  return join(projectRoot, ".omx", "setup-scope.json");
}