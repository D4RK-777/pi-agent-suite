# 07 — Customization

How to extend Pi Agent Suite with your own agents, skills, and bundles.

---

## Adding a new agent

### Step 1 — Copy the template

```bash
cp -r ~/.pi/agent/agents/_template ~/.pi/agent/agents/my-agent
```

### Step 2 — Write the AGENT.md system prompt

Edit `~/.pi/agent/agents/my-agent/AGENT.md`:

```markdown
# My Agent — [Role Name]

You are a specialist in [domain]. Your job is to [primary purpose].

## Responsibilities

- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

## What you are NOT responsible for

- [Out of scope 1]
- [Out of scope 2]

## How to handle tasks

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Output standards

- [Standard 1]
- [Standard 2]

## Skills available to you

- `auto-memory` — persist patterns and decisions
- `mempalace-tools` — search your memory
- `pi-tasks` — create and track tasks
```

### Step 3 — Create the manifest

Create `~/.pi/agent/manifests/my-agent.json`:

```json
{
  "name": "my-agent",
  "aliases": ["my", "myagent"],
  "role": "Specialist in [domain]",
  "domain_focus": ["keyword1", "keyword2", "keyword3"],
  "skill_keywords": ["specific", "task", "words"],
  "tags": ["tag1", "tag2"],
  "skills": ["auto-memory", "mempalace-tools", "pi-tasks"],
  "system_prompt_file": "agents/my-agent/AGENT.md",
  "note": "Use when the task involves [description]"
}
```

### Step 4 — Register with the brain router

Edit `~/.pi/agent/brain/router.py`, add to `SKILL_REGISTRY`:

```python
SKILL_REGISTRY = {
    # ... existing entries ...
    "my-agent": {
        "keywords": ["keyword1", "keyword2", "specific-term"],
        "aliases": ["my", "myagent"],
        "tags": ["tag1", "tag2"],
        "domain": ["domain1", "domain2"],
    }
}
```

And add to `SKILL_DESCRIPTIONS`:
```python
SKILL_DESCRIPTIONS = {
    # ... existing entries ...
    "my-agent": "Handles [description of what this agent does]"
}
```

### Step 5 — Test routing

```bash
cd ~/.pi/agent
python -m harness route "task that should go to my-agent"
```

---

## Adding a new skill

Skills are markdown files that describe a capability. Agents reference them by name.

### Create the skill file

Create `~/.pi/agent/skills/my-skill.md`:

```markdown
# My Skill

## When to use this skill

Use when [condition].

## What this skill enables

- [Capability 1]
- [Capability 2]

## Procedure

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Output format

[How to format output when using this skill]

## Constraints

- [Constraint 1]
- [What NOT to do]
```

### Register with the brain router

Add your skill keyword triggers to `brain/router.py` SKILL_REGISTRY for the agents that should have it.

### Reference in agent manifests

Add the skill name to agent manifests:
```json
{
  "skills": ["auto-memory", "mempalace-tools", "my-skill"]
}
```

---

## Creating a bundle

Bundles are JSON files that group related skills together.

Create `~/.pi/agent/bundles/my-bundle.json`:

```json
{
  "name": "my-bundle",
  "description": "Skills for [use case]",
  "skills": [
    "auto-memory",
    "mempalace-tools",
    "my-skill",
    "pi-tasks"
  ],
  "agents": ["my-agent", "backend", "reviewer"],
  "recommended_for": "tasks involving [description]"
}
```

Use a bundle:
```bash
python -m harness route "my task" --bundle my-bundle
```

---

## Writing a cookbook

Cookbooks are multi-step workflow templates.

Create `~/.pi/agent/cookbooks/my-workflow.md`:

```markdown
# My Workflow Cookbook

## When to use

Use for [scenario]. Typically takes [time estimate].

## Steps

### Step 1 — [Step name] (agent: scout)
**Input:** [What this step receives]
**Task:** [What to do]
**Output:** [What this step produces]
**Handoff:** Pass [X] to Step 2.

### Step 2 — [Step name] (agent: backend)
**Input:** [X from Step 1]
**Task:** [What to do]
**Output:** [What this step produces]
**Handoff:** Pass [Y] to Step 3.

### Step 3 — [Step name] (agent: reviewer)
**Input:** [Y from Step 2]
**Task:** Review [Z] for [criteria].
**Output:** Approved implementation or list of changes needed.

## Success criteria

- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Rollback

If Step 2 fails: [What to do]
If Step 3 fails: [What to do]
```

---

## Customizing memory behavior

### Change the auto-mine interval

```bash
export MEMPAL_SAVE_INTERVAL=10   # mine every 10 exchanges (more frequent)
export MEMPAL_SAVE_INTERVAL=30   # mine every 30 exchanges (less frequent)
```

### Add a directory that always gets mined

```bash
export MEMPAL_INGEST_DIR="~/my-project/docs"
# Now mempal_save_hook.sh will mine this dir on every Stop event
```

### Mine additional wings

In `mempalace_prompt_hook.py`, you can adjust which wings are searched:

```python
results = search(prompt_text, wing="code", n=3)     # code wing only
results = search(prompt_text, n=5)                   # all wings, top 5
```

---

## Customizing the prompt injection

Edit `~/.pi/agent/bin/mempalace_prompt_hook.py` to change what gets injected:

```python
# Change result count
results = search(prompt_text, n=5)  # default is 3

# Filter by wing
results = search(prompt_text, wing="decisions", n=3)

# Change output format
for r in results.get("results", []):
    # Customize the injected text format here
    print(f"<mempalace-context wing='{r.get('wing')}'>")
    print(r["content"][:800])  # default is 500 chars
    print("</mempalace-context>")
```

---

## Personalizing the vault

The vault template at `vault-template/` is a starting point. Personalize it:

1. **Add your raw sources**: Drop documents into `raw/articles/` or `raw/books/`
2. **Run ingest**: Ask Claude Code to `ingest raw/articles/my-document.md`
3. **Add patterns**: Create `patterns/{slug}.md` for your coding patterns
4. **Add decisions**: Log architectural choices in `decisions/YYYY-MM-DD-{slug}.md`

The wiki grows automatically as you ingest more sources. The `hot.md` file keeps your most recent 10-15 concepts warm.

---

## Environment-based customization

All key behaviors can be tuned via environment variables without editing code:

```bash
# ~/.pi/env.sh (or env.ps1 on Windows)
export PI_AGENT_HOME="$HOME/.pi"
export MEMPALACE_PALACE="$HOME/.mempalace/palace"
export MEMPAL_SAVE_INTERVAL=15
export MEMPAL_INGEST_DIR=""
export OBSIDIAN_VAULT="$HOME/MyVault"
export OBSIDIAN_API_KEY="your-key"
export OBSIDIAN_VAULT_NAME="MyVault"
```

---

## Sharing your customizations

If you build an agent or skill that others would find useful:

1. Add it to `agent/agents/`, `agent/manifests/`, `agent/skills/`
2. Document it in the file itself (AGENT.md or skill.md)
3. Open a PR to the pi-agent-suite repo

Contributions welcome — especially domain-specific agents (data science, DevOps, mobile, etc.).
