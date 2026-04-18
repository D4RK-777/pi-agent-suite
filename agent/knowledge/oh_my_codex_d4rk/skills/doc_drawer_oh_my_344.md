name (search both scopes)
2. **Parse YAML frontmatter** and content
3. **Display complete details:**

```
Skill: custom-logger
Scope: user (~/.codex/skills/custom-logger/)
Description: Enhanced logging with structured output
Triggers: log, logger, logging
Argument Hint: <level> [message]
Quality: 95% (if available)
Usage Count: 42 times (if available)
File Path: /home/user/.codex/skills/custom-logger/SKILL.md

--- FULL CONTENT ---
[entire markdown content]
```

**If not found:** Report error with suggestion to use `/skill search`

**Example:**
```
User: /skill info custom-logger
Assistant: Skill: custom-logger
Scope: user
Description: Enhanced logging with structured output
Triggers: log, logger, logging
File: ~/.codex/skills/custom-logger/SKILL.md

--- CONTENT ---
# Custom Logger Skill