inalExitCode;
  return { stdout: stdoutChunks.join(''), stderr: stderrChunks.join(''), exitCode };
}

async function createExploreTestPath(wd: string): Promise<string> {
  const binDir = join(wd, 'test-bin');
  await mkdir(binDir, { recursive: true });
  const rgPath = join(binDir, process.platform === 'win32' ? 'rg.cmd' : 'rg');
  const lines = process.platform === 'win32'
    ? ['@echo off', 'echo ripgrep 14.0.0', '']
    : ['#!/bin/sh', 'echo "ripgrep 14.0.0"', ''];
  await writeFile(rgPath, lines.join(process.platform === 'win32' ? '\r\n' : '\n'));
  if (process.platform !== 'win32') {
    await chmod(rgPath, 0o755);
  }
  return `${binDir}${process.platform === 'win32' ? ';' : ':'}${process.env.PATH || ''}`;
}