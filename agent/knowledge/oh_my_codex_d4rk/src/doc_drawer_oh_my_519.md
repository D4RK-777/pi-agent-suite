getPackageRoot()): string {
  return join(pkgRoot, "dist", "scripts", "hook-derived-watcher.js");
}

export function resolveNotifyHookScript(pkgRoot = getPackageRoot()): string {
  return join(pkgRoot, "dist", "scripts", "notify-hook.js");
}

const HELP = `
oh-my-codex (omx) - Multi-agent orchestration for Codex CLI

Usage:
  omx           Launch Codex CLI (HUD auto-attaches only when already inside tmux)
  omx exec      Run codex exec non-interactively with OMX AGENTS/overlay injection
  omx setup     Install skills, prompts, MCP servers, and scope-specific AGENTS.md
  omx uninstall Remove OMX configuration and clean up installed artifacts
  omx doctor    Check installation health
  omx cleanup   Kill orphaned OMX MCP server processes and remove stale OMX /tmp directories