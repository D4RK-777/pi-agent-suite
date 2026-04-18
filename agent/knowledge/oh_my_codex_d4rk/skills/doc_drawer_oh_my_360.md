- [Integration-specific pitfall #1]
- [Integration-specific pitfall #2]
```

---

## Error Handling

**All commands must handle:**
- File/directory doesn't exist
- Permission errors
- Invalid YAML frontmatter
- Duplicate skill names
- Invalid skill names (spaces, special chars)

**Error format:**
```
✗ Error: <clear message>
→ Suggestion: <helpful next step>
```

---

## Usage Examples

```bash
# List all skills
/skill list

# Create a new skill
/skill add my-custom-skill

# Remove a skill
/skill remove old-skill

# Edit existing skill
/skill edit error-handler

# Search for skills
/skill search typescript error

# Get detailed info
/skill info my-custom-skill

# Sync between scopes
/skill sync

# Run setup wizard
/skill setup

# Quick scan
/skill scan
```

## Usage Modes