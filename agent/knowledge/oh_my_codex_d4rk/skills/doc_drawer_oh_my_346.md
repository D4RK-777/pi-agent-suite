- test-runner
  - backend-scaffold

Common skills (3):
  - frontend-ui-ux
  - git-master
  - planner

Options:
  [1] Copy user skill to project
  [2] Copy project skill to user
  [3] View differences
  [4] Cancel
```

4. **Handle user choice:**
   - Option 1: Select skill(s) to copy to project
   - Option 2: Select skill(s) to copy to user
   - Option 3: Show side-by-side diff for common skills
   - Option 4: Exit

**Safety:** Never overwrite without confirmation

**Example:**
```
User: /skill sync
Assistant: Found 5 user-only skills and 2 project-only skills.

Copy 'error-handler' from user to project? (yes/no/skip)
User: yes
Assistant: ✓ Copied 'error-handler' to .codex/skills/

Copy 'api-builder' from user to project? (yes/no/skip)
User: skip
...
```

---

### /skill setup