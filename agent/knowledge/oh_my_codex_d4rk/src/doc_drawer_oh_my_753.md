rn) {
    console.log(`Migration hint: ${legacySkillOverlapNotice.message}`);
    console.log();
  }

  if (force) {
    console.log(
      "Force mode: enabled additional destructive maintenance (for example stale deprecated skill cleanup).",
    );
    console.log();
  }

  console.log('Setup complete! Run "omx doctor" to verify installation.');
  console.log("\nNext steps:");
  console.log("  1. Start Codex CLI in your project directory");
  console.log(
    "  2. Use role/workflow keywords like $architect, $executor, and $plan in Codex",
  );
  console.log("  3. Browse skills with /skills; AGENTS keyword routing can also activate them implicitly");
  console.log("  4. The AGENTS.md orchestration brain is loaded automatically");
  console.log(