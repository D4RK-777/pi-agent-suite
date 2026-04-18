const repoBuilt = repoBuiltExploreHarnessCommand(packageRoot);
  if (repoBuilt) return repoBuilt;

  const manifestPath = join(packageRoot, 'crates', 'omx-explore', 'Cargo.toml');
  if (!existsSync(manifestPath)) {
    throw new Error(`[explore] neither a compatible packaged harness binary nor Rust manifest was found (${manifestPath})`);
  }

  return {
    command: 'cargo',
    args: ['run', '--quiet', '--manifest-path', manifestPath, '--'],
  };
}