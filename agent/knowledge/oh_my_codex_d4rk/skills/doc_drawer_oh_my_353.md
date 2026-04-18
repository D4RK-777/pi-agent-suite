rom URL or paste content
5. **Done** - Exit the wizard

**Option 3: Scan Conversation for Patterns**

Analyze the current conversation context to identify potential skill-worthy patterns. Look for:
- Recent debugging sessions with non-obvious solutions
- Tricky bugs that required investigation
- Codebase-specific workarounds discovered
- Error patterns that took time to resolve

Report findings and ask if user wants to extract any as skills (invoke `/learner` if yes).

**Option 4: Import Skill**

Ask user to provide either:
- **URL**: Download skill from a URL (e.g., GitHub gist)
- **Paste content**: Paste skill markdown content directly

Then ask for scope:
- **User-level** (~/.codex/skills/) - Available across all projects
- **Project-level** (.codex/skills/) - Only for this project