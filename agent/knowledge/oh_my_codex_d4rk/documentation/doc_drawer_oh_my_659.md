parkshell tmux-pane smoke | `node bin/omx.js sparkshell --tmux-pane %2141 --tail-lines 120` | PASS |
| Full test suite | `npm test` | PASS (`2375` pass / `0` fail) |
| Packed tarball dry run | `npm pack --dry-run` | PASS (`oh-my-codex-0.9.0.tgz`) |
| Explore verification lane | `npm run test:explore` | PASS (`39` pass / `0` fail) |
| Sparkshell verification lane | `npm run test:sparkshell` | PASS (Rust suites passed: `32 + 11 + 5`, `0` fail) |

## Current release-shape evidence

- current package version: `0.9.0`
- latest existing git tag in repo: `v0.8.15`
- current branch: `dev`
- unreleased head vs tag: **55 non-merge commits**
- unreleased diff vs tag: **149 files changed, +12,325 / -254**

## Remaining release actions