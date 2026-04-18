/docs. |

## Verification checklist after upgrade

Run this checklist after pulling latest mainline:

- [ ] Confirm removed references are gone from local notes/scripts:
  ```bash
  rg -n "deep-executor|scientist|pipeline|project-session-manager|\bpsm\b|ultrapilot|learn-about-omx|writer-memory|learner|deepinit|\brelease\b" README.md docs scripts .omx -S
  ```
- [ ] Confirm current prompt catalog no longer contains removed prompts:
  ```bash
  ls prompts
  ```
- [ ] Confirm current skill catalog no longer contains removed skills:
  ```bash
  ls skills
  ```
- [ ] Validate setup scope options are available:
  ```bash
  omx help | rg -e "--scope|project"
  ```
- [ ] Validate team/tmux health checks:
  ```bash
  omx doctor --team
  ```