{JSON.stringify(blockedStdoutPath)} 2> ${JSON.stringify(blockedStderrPath)}
blocked_status=$?
set -e

{
  printf 'PATH=%s\n' "$PATH"
  printf 'SHELL=%s\n' "\${SHELL:-}"
  printf 'ALLOWED_STATUS=%s\n' "$allowed_status"
  printf 'BLOCKED_STATUS=%s\n' "$blocked_status"
  printf -- '--ARGV--\n'
  cat ${JSON.stringify(argvPath)}
  printf -- '--ALLOWED_STDOUT--\n'
  cat ${JSON.stringify(allowedStdoutPath)}
  printf -- '--ALLOWED_STDERR--\n'
  cat ${JSON.stringify(allowedStderrPath)}
  printf -- '--BLOCKED_STDOUT--\n'
  cat ${JSON.stringify(blockedStdoutPath)}
  printf -- '--BLOCKED_STDERR--\n'
  cat ${JSON.stringify(blockedStderrPath)}
} > ${JSON.stringify(capturePath)}

printf '# Answer\nHarness completed\n' > "$output_path"
`,
  );
  await chmod(stub, 0o755);
  return stub;
}