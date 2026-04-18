ecision.reason})` : "";
      console.log(`  ${label} ${relativeDir}/AGENTS.md${reason}`);
    }
  }

  console.log("\nGuardrails:");
  console.log(
    "- Generates the target directory and its direct child directories only.",
  );
  console.log(
    "- Skips generated/vendor/build directories via a fixed exclusion list.",
  );
  console.log(
    "- Preserves manual notes only for files already managed by omx agents-init.",
  );
  console.log(
    "- Never overwrites unmanaged AGENTS.md files unless you pass --force.",
  );
  console.log(
    "- Avoids rewriting project-root AGENTS.md while an active omx session is running.\n",
  );