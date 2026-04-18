lude new sections:
`## OMX Posture Overlay`, `## Model-Class Guidance`, and `## OMX Agent Metadata`.

Representative routing:
- `planner` / `architect` / `critic` -> `frontier-orchestrator`
- `executor` / `build-fixer` / `test-engineer` -> `deep-worker`
- `explore` / `writer` -> `fast-lane`

PRs: [#588](https://github.com/Yeachan-Heo/oh-my-codex/pull/588), [#592](https://github.com/Yeachan-Heo/oh-my-codex/pull/592) ([@HaD0Yun](https://github.com/HaD0Yun))

## Bug fixes

### Windows ESM import crash

`bin/omx.js` failed on Windows with `ERR_UNSUPPORTED_ESM_URL_SCHEME` because `import()` received a bare absolute path (`C:\...`) instead of a `file://` URL.

Fix: convert the resolved path to a `file://` URL via `url.pathToFileURL()` before dynamic import.