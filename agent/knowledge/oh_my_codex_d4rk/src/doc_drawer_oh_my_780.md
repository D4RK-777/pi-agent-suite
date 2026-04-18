console.log(`  ${prefix} ${staleSkill}/ (status: ${label})`);
      }
    }
  }

  return summary;
}

async function updateManagedConfig(
  configPath: string,
  pkgRoot: string,
  sharedMcpRegistry: UnifiedMcpRegistryLoadResult,
  summary: SetupCategorySummary,
  backupContext: SetupBackupContext,
  options: Pick<
    SetupOptions,
    "codexVersionProbe" | "dryRun" | "verbose" | "modelUpgradePrompt"
  >,
): Promise<ManagedConfigResult> {
  const existing = existsSync(configPath)
    ? await readFile(configPath, "utf-8")
    : "";
  const currentModel = getRootModelName(existing);
  let modelOverride: string | undefined;
  const codexVersion =
    options.codexVersionProbe?.() ?? probeInstalledCodexVersion();
  const omxManagesTui = shouldOmxManageTuiFromCodexVersion(codexVersion);