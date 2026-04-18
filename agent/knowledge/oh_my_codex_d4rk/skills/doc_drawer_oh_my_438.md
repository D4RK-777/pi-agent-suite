pass/fail)
  - qualitative signal (`reasoning`, `suggestions`, `next_actions`)
</Threshold_And_Loop>

<Debug_Visualization>
When mismatch diagnosis is hard:
1. Keep `$visual-verdict` as the authoritative decision.
2. Use pixel-level diff tooling (pixel diff / pixelmatch overlay) as a **secondary debug aid** to localize hotspots.
3. Convert pixel diff hotspots into concrete `differences[]` and `suggestions[]` updates.
</Debug_Visualization>