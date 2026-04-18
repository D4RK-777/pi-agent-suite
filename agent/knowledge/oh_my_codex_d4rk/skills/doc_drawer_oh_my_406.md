Required Reporting During Execution

When operating this skill, provide concrete progress evidence:

1. Team started line (`Team started: <name>`)
2. tmux target and worker pane presence
3. leader mailbox ACK path/content check
4. status/shutdown outcomes

Do not claim success without file/pane evidence.
Do not claim clean completion if shutdown occurred with `in_progress>0`.
Use `omx sparkshell --tmux-pane ...` as an explicit opt-in operator aid for pane inspection and summaries; keep raw `tmux capture-pane` evidence available for manual intervention and proof.

## MCP Job Lifecycle Tools

For programmatic or agent-driven team spawning (as opposed to interactive CLI use), OMX exposes four MCP tools via the `team-server`: