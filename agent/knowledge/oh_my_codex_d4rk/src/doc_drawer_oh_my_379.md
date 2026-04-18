available.
  <mission-dir>    Directory inside a git repository containing mission.md and sandbox.md
  <run-id>         Existing autoresearch run id from .omx/logs/autoresearch/<run-id>/manifest.json

Behavior:
  - deep-interview intake writes canonical artifacts under .omx/specs before launch
  - validates mission.md and sandbox.md
  - requires sandbox.md YAML frontmatter with evaluator.command and evaluator.format=json
  - fresh launch creates a run-tagged autoresearch/<slug>/<run-tag> lane
  - supervisor records baseline, candidate, keep/discard/reset, and results artifacts under .omx/logs/autoresearch/
  - run prefers interview|autoresearch split-pane launch inside tmux, with foreground fallback on failure