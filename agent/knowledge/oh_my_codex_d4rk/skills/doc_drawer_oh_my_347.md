s/

Copy 'api-builder' from user to project? (yes/no/skip)
User: skip
...
```

---

### /skill setup

Interactive wizard for setting up and managing local skills (formerly local-skills-setup).

**Behavior:**

#### Step 1: Directory Check and Setup

First, check if skill directories exist and create them if needed:

```bash
# Check and create user-level skills directory
USER_SKILLS_DIR="$HOME/.codex/skills"
if [ -d "$USER_SKILLS_DIR" ]; then
  echo "User skills directory exists: $USER_SKILLS_DIR"
else
  mkdir -p "$USER_SKILLS_DIR"
  echo "Created user skills directory: $USER_SKILLS_DIR"
fi