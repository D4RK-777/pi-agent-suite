terminalized/non-active.
4. Cancellation MUST remain scope-safe: no mutation of unrelated sessions.

See: `docs/contracts/ralph-cancel-contract.md`.

Active modes are still cancelled in dependency order:
1. Autopilot (includes linked ralph/ultraqa/ecomode cleanup)
2. Ralph (cleans its linked ultrawork or ecomode)
3. Ultrawork (standalone)
4. Ecomode (standalone)
5. UltraQA (standalone)
6. Swarm (standalone)
7. Ultrapilot (standalone)
8. Pipeline (standalone)
9. Team (tmux-based)
10. Plan Consensus (standalone)

## Normative Ralph post-conditions (MUST)

When cancellation targets Ralph state in a scope, completion requires all of the following: