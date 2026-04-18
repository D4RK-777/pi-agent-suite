kageJsonPath(packageRoot = getPackageRoot()): string {
  return join(packageRoot, 'package.json');
}

async function readPackageJson(packageRoot = getPackageRoot()): Promise<{ version?: string; repository?: { url?: string } | string }> {
  const raw = await readFile(packageJsonPath(packageRoot), 'utf-8');
  return JSON.parse(raw) as { version?: string; repository?: { url?: string } | string };
}

export async function getPackageVersion(packageRoot = getPackageRoot()): Promise<string> {
  const pkg = await readPackageJson(packageRoot);
  if (!pkg.version?.trim()) throw new Error('[native-assets] package.json is missing version');
  return pkg.version.trim();
}