el_reasoning_effort, developer_instructions)",
      );
    }
    if (summary.featureFlagsRemoved) {
      console.log("    Feature flags (multi_agent, child_agents_md)");
    }
  } else if (!summary.configCleaned && summary.mcpServersRemoved.length === 0) {
    console.log("  config.toml: no OMX entries found (or --keep-config used)");
  }

  if (summary.promptsRemoved > 0) {
    console.log(`  ${prefix} ${summary.promptsRemoved} agent prompt(s)`);
  }
  if (summary.skillsRemoved > 0) {
    console.log(`  ${prefix} ${summary.skillsRemoved} skill(s)`);
  }
  if (summary.agentConfigsRemoved > 0) {
    console.log(
      `  ${prefix} ${summary.agentConfigsRemoved} native agent config(s)`,
    );
  }
  if (summary.agentsMdRemoved) {
    console.log(`  ${prefix} AGENTS.md`);
  }