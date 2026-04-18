user

#### If Autopilot Active

Call `cancelAutopilot()` from `src/hooks/autopilot/cancel.ts:27-78`:

```bash
# Autopilot handles its own cleanup + ralph + ultraqa
# Just mark autopilot as inactive (preserves state for resume)
if [[ -f .omx/state/autopilot-state.json ]]; then
  # Clean up ralph if active
  if [[ -f .omx/state/ralph-state.json ]]; then
    RALPH_STATE=$(cat .omx/state/ralph-state.json)
    LINKED_UW=$(echo "$RALPH_STATE" | jq -r '.linked_ultrawork // false')

    # Clean linked ultrawork first
    if [[ "$LINKED_UW" == "true" ]] && [[ -f .omx/state/ultrawork-state.json ]]; then
      rm -f .omx/state/ultrawork-state.json
      echo "Cleaned up: ultrawork (linked to ralph)"
    fi