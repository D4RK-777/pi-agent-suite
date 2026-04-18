# Google AI Studio / Gemini Adapter

Use this adapter when wiring Google AI Studio or Gemini environments to the D4rkMynd shared library.

## Model

- Keep shared reusable skills in `%PI_AGENT_HOME%\skills`.
- Google AI Studio uses prompt instructions and system prompts for persistent behavior.
- Keep repo-specific instructions in repo-local `AGENTS.md` and generated wrapper files.

## Typical Targets

- Google AI Studio system prompt
- Project context files

## Recommended Actions

Use `..\..\scripts\sync-skills.ps1` for canonical bulk sync.

Use `..\..\scripts\generate-modes.ps1 -ProjectPath <repo>` when the active repo should expose generated wrapper files alongside `AGENTS.md`.

## Universal Mode Setup

Google AI Studio accepts system instructions in the prompt setup.

To enable universal routing:
1. Run `powershell -ExecutionPolicy Bypass -File %PI_AGENT_HOME%\scripts\generate-modes.ps1`
2. Copy the generated `.cursorrules-auto` content to your Google AI Studio system instructions
3. Google AI Studio will now route automatically using the D4rkMynd router

## System Prompt Template

```
You are operating within the D4rkMynd agent system. Before responding to any user request:

1. Analyze the request to determine which specialist agent should handle it
2. Load the appropriate skill files from %PI_AGENT_HOME%\skills\
3. Follow the skill instructions exactly
4. Do not improvise or deviate from the skill patterns

Routing decision table:
- Vague/cross-domain → d4rkmynd (overseer)
- Advice/second opinion → advisor
- UI/components/styling → frontend
- APIs/database → backend
- Security review → security
- Incidents/monitoring → reliability
- Login/auth/sessions → auth
- Code review → reviewer
- Testing → tester
- Debugging → debugger
- Cleanup/refactoring → refactorer
- Work splitting → manager
- Research → scout
```
