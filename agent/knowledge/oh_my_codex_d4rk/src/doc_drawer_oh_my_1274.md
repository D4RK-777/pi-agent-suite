# Answer\nHarness completed\n' > "$output_path"
`,
  );
  await chmod(stub, 0o755);
  return stub;
}

async function writeScenarioCodexStub(wd: string, body: string): Promise<string> {
  const stub = join(wd, 'codex-scenario-stub.sh');
  await writeFile(
    stub,
    `#!/bin/sh
set -eu
output_path=''
model=''
while [ "$#" -gt 0 ]; do
  case "$1" in
    -o)
      output_path="$2"
      shift 2
      ;;
    -m)
      model="$2"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done
if [ -z "$output_path" ]; then
  printf 'missing -o output path\n' >&2
  exit 1
fi
if [ -z "$model" ]; then
  printf 'missing -m model\n' >&2
  exit 1
fi
${body}
`,
  );
  await chmod(stub, 0o755);
  return stub;
}