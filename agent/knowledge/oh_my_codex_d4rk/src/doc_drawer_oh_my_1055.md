ng' ? body.version : null;
  } catch {
    return null;
  } finally {
    clearTimeout(timer);
  }
}

async function getCurrentVersion(): Promise<string | null> {
  try {
    const pkgPath = join(getPackageRoot(), 'package.json');
    const content = await readFile(pkgPath, 'utf-8');
    const pkg = JSON.parse(content) as { version?: string };
    return typeof pkg.version === 'string' ? pkg.version : null;
  } catch {
    return null;
  }
}

function runGlobalUpdate(): { ok: boolean; stderr: string } {
  const result = spawnSync('npm', ['install', '-g', `${PACKAGE_NAME}@latest`], {
    encoding: 'utf-8',
    stdio: ['ignore', 'ignore', 'pipe'],
    timeout: 120000,
  });