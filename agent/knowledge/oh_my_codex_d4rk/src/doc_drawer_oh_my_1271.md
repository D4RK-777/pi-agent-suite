55);
  }
  return `${binDir}${process.platform === 'win32' ? ';' : ':'}${process.env.PATH || ''}`;
}

async function writeEnvNodeCodexStub(wd: string, capturePath: string): Promise<string> {
  const stub = join(wd, 'codex-stub.sh');
  const argvPath = join(wd, 'codex-argv.txt');
  const allowedStdoutPath = join(wd, 'allowed.stdout.txt');
  const allowedStderrPath = join(wd, 'allowed.stderr.txt');
  const blockedStdoutPath = join(wd, 'blocked.stdout.txt');
  const blockedStderrPath = join(wd, 'blocked.stderr.txt');
  await writeFile(
    stub,
    `#!/bin/sh
set -eu
output_path=''
: > ${JSON.stringify(argvPath)}
while [ "$#" -gt 0 ]; do
  printf '%s\n' "$1" >> ${JSON.stringify(argvPath)}
  if [ "$1" = "-o" ] && [ "$#" -ge 2 ]; then
    output_path="$2"
    shift 2
    continue
  fi
  shift