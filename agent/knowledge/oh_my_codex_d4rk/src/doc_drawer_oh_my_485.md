'[explore] sparkshell backend is incompatible with this Linux runtime (missing GLIBC symbols)');
  }

  if (result.stdout && result.stdout.length > 0) process.stdout.write(result.stdout);
  if (result.stderr && result.stderr.length > 0) process.stderr.write(result.stderr);

  if (result.status !== 0) {
    process.exitCode = result.status ?? 1;
  }
}

export function packagedExploreHarnessBinaryName(platform: NodeJS.Platform = process.platform): string {
  return platform === 'win32' ? 'omx-explore-harness.exe' : 'omx-explore-harness';
}