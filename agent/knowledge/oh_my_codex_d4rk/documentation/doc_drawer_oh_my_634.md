ss `omx-explore` and `omx-sparkshell` summarization with outputs that bury signal under distractors.

**Setup**
1. Build 3-10 text fixtures with:
   - one clear critical failure/success fact,
   - many distractor lines,
   - at least one actionable next-step hint,
   - optional conflicting near-miss distractors.
2. For each fixture, write the must-preserve facts before running the tool.

Suggested corpus dimensions:
- duplicated near-match file paths,
- multiple warnings with one real blocker,
- success text followed by later failure text,
- long tails where the important line appears early, middle, and late.

**Evidence to capture**
- fixture id,
- must-preserve fact list,
- observed summarized output,
- missing/preserved fact checklist.