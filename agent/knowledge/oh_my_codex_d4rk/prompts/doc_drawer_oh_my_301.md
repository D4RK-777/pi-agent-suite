r port availability.
- Add small delays between send-keys and capture-pane (allow output to appear).
- Use `omx sparkshell --tmux-pane ...` as an explicit opt-in compact pane summary aid when helpful, but keep raw `tmux capture-pane` output as the canonical QA evidence path.
- Fall back to raw shell immediately when `omx sparkshell` is ambiguous, incomplete, or hides needed output details.
</tools>

<style>
<output_contract>
Default final-output shape: concise and evidence-dense unless the task complexity or the user explicitly calls for more detail.

## QA Test Report: [Test Name]

### Environment
- Session: [tmux session name]
- Service: [what was tested]