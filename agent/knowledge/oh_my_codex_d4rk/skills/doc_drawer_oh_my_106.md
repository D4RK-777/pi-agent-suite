f UltraQA Active (standalone)

Call `clearUltraQAState()` from `src/hooks/ultraqa/index.ts:107-120`:

```bash
if [[ -f .omx/state/ultraqa-state.json ]]; then
  rm -f .omx/state/ultraqa-state.json
  echo "UltraQA cancelled. QA cycling workflow stopped."
fi
```

#### No Active Modes

```bash
echo "No active OMX modes detected."
echo ""
echo "Checked for:"
echo "  - Autopilot (.omx/state/autopilot-state.json)"
echo "  - Ralph (.omx/state/ralph-state.json)"
echo "  - Ultrawork (.omx/state/ultrawork-state.json)"
echo "  - UltraQA (.omx/state/ultraqa-state.json)"
echo ""
echo "Use --force to clear all state files anyway."
```

## Implementation Notes