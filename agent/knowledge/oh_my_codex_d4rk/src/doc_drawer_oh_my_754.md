y");
  console.log("  4. The AGENTS.md orchestration brain is loaded automatically");
  console.log(
    "  5. Native agent defaults configured in config.toml [agents] and TOML files written to .codex/agents/",
  );
  console.log(
    '  6. "omx explore" and "omx sparkshell" can hydrate native release binaries on first use; source installs still allow repo-local fallbacks and OMX_EXPLORE_BIN / OMX_SPARKSHELL_BIN overrides',
  );
  if (isGitHubCliConfigured()) {
    console.log("\nSupport the project: gh repo star Yeachan-Heo/oh-my-codex");
  }
}

function isLegacySkillPromptShim(content: string): boolean {
  const marker =
    /Read and follow the full skill instructions at\s+.*\/skills\/[^/\s]+\/SKILL\.md/i;
  return marker.test(content);
}