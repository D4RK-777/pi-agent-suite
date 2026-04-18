-progress.json`.
- Keep legacy files unchanged for one release cycle.

## Background Execution Rules

**Run in background** (`run_in_background: true`):
- Package installation (npm install, pip install, cargo build)
- Build processes (make, project build commands)
- Test suites
- Docker operations (docker build, docker pull)

**Run blocking** (foreground):
- Quick status checks (git status, ls, pwd)
- File reads and edits
- Simple commands
</Advanced>

Original task:
{{PROMPT}}