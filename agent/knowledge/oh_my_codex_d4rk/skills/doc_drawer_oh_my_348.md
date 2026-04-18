_DIR"
else
  mkdir -p "$USER_SKILLS_DIR"
  echo "Created user skills directory: $USER_SKILLS_DIR"
fi

# Check and create project-level skills directory
PROJECT_SKILLS_DIR=".codex/skills"
if [ -d "$PROJECT_SKILLS_DIR" ]; then
  echo "Project skills directory exists: $PROJECT_SKILLS_DIR"
else
  mkdir -p "$PROJECT_SKILLS_DIR"
  echo "Created project skills directory: $PROJECT_SKILLS_DIR"
fi
```

#### Step 2: Skill Scan and Inventory

Scan both directories and show a comprehensive inventory:

```bash
# Scan user-level skills
echo "=== USER-LEVEL SKILLS (~/.codex/skills/) ==="
if [ -d "$HOME/.codex/skills" ]; then
  USER_COUNT=$(find "$HOME/.codex/skills" -name "*.md" 2>/dev/null | wc -l)
  echo "Total skills: $USER_COUNT"