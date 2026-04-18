view workflows"

**If no security-reviewer usage:**
- "Use security-reviewer after auth/API changes"

**If defaultExecutionMode not set:**
- "Set defaultExecutionMode in /omx-setup for consistent behavior"

### Step 4: Output Report

Format a summary with:
- Token summary (total, by model)
- Top agents used
- Underutilized features
- Personalized recommendations

### Example Output

```
📊 Your OMX Usage Analysis

TOKEN SUMMARY:
- Total records: 1,234
- By Reasoning Effort: high 45%, medium 40%, low 15%

TOP AGENTS:
1. executor (234 uses)
2. architect (89 uses)
3. explore (67 uses)

UNDERUTILIZED FEATURES:
- ecomode: 0 uses (could save ~30% on routine tasks)
- team: 0 uses (great for coordinated workflows)