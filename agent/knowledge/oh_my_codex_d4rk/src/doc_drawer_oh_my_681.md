text...]
  omx ralph --prd "<task text>"
  omx ralph [ralph-options] [codex-args...] [task text...]

Options:
  --help, -h           Show this help message
  --prd <task text>    PRD mode shortcut: mark the task text explicitly
  --prd=<task text>    Same as --prd "<task text>"
  --no-deslop         Skip the final ai-slop-cleaner pass

PRD mode:
  Ralph initializes persistence artifacts in .omx/ so PRD and progress
  state can survive across Codex sessions. Provide task text either as
  positional words or with --prd.

Common patterns:
  omx ralph "Fix flaky notify-hook tests"
  omx ralph --prd "Ship release checklist automation"
  omx ralph --model gpt-5 "Refactor state hydration"
  omx ralph -- --task-with-leading-dash
`;