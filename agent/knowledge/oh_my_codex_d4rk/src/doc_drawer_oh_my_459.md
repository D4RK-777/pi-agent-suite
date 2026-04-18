}
  return { name: 'Node.js', status: 'fail', message: `v${process.versions.node} (need >= 20)` };
}

function checkExploreHarness(): Check {
  const packageRoot = getPackageRoot();
  const manifestPath = join(packageRoot, 'crates', 'omx-explore', 'Cargo.toml');
  if (!existsSync(manifestPath)) {
    return {
      name: 'Explore Harness',
      status: 'warn',
      message: 'Rust harness sources not found in this install (omx explore unavailable until packaged or OMX_EXPLORE_BIN is set)',
    };
  }