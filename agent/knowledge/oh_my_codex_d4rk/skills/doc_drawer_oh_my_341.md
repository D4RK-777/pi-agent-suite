el` - Exit without changes
5. **For selected field:**
   - Show current value
   - Ask for new value
   - Update YAML frontmatter or content
   - Write back to file
6. **Report success** with summary of changes

**Example:**
```
User: /skill edit custom-logger
Assistant: Current skill 'custom-logger':
  - Description: Enhanced logging with structured output
  - Triggers: log, logger, logging
  - Argument hint: <level> [message]

What would you like to edit? (description/triggers/argument-hint/content/rename/cancel)

User: triggers
Assistant: Current triggers: log, logger, logging
New triggers (comma-separated): log, logger, logging, trace

✓ Updated triggers for 'custom-logger'
```

---

### /skill search <query>

Search skills by content, triggers, name, or description.