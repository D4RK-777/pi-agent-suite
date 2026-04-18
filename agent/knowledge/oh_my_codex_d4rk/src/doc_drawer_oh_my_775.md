e agent";
      console.log(`  ${prefix} ${file}`);
    }
    removed += 1;
  }

  return removed;
}

export async function installSkills(
  srcDir: string,
  dstDir: string,
  backupContext: SetupBackupContext,
  options: SetupOptions,
): Promise<SetupCategorySummary> {
  const summary = createEmptyCategorySummary();
  if (!existsSync(srcDir)) return summary;
  const installableSkills: Array<{
    name: string;
    sourceDir: string;
    destinationDir: string;
  }> = [];
  const manifest = tryReadCatalogManifest();
  const skillStatusByName = manifest
    ? new Map(manifest.skills.map((skill) => [skill.name, skill.status]))
    : null;
  const isInstallableStatus = (status: string | undefined): boolean =>
    status === "active" || status === "internal";