f [ "$1" = "-o" ] && [ "$#" -ge 2 ]; then
    output_path="$2"
    shift 2
    continue
  fi
  shift
done

if [ -z "$output_path" ]; then
  printf 'missing -o output path\n' >&2
  exit 1
fi

bash -lc 'rg --version' > ${JSON.stringify(allowedStdoutPath)} 2> ${JSON.stringify(allowedStderrPath)}
allowed_status=$?
set +e
bash -lc 'node --version' > ${JSON.stringify(blockedStdoutPath)} 2> ${JSON.stringify(blockedStderrPath)}
blocked_status=$?
set -e