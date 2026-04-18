UTORESEARCH_HELP = `omx autoresearch - Launch OMX autoresearch with thin-supervisor parity semantics

Usage:
  omx autoresearch                                                (human entrypoint: launch Codex CLI deep-interview intake, then execute)
  omx autoresearch [--topic T] [--evaluator CMD] [--keep-policy P] [--slug S]
  omx autoresearch init [--topic T] [--evaluator CMD] [--keep-policy P] [--slug S]
  omx autoresearch run <mission-dir> [codex-args...]              (agent/explicit execution entrypoint)
  omx autoresearch <mission-dir> [codex-args...]                  (compatibility alias for run)
  omx autoresearch --resume <run-id> [codex-args...]