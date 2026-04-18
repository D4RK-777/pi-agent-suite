dLegacyPromptShims;
    if (cleanedLegacyPromptShims > 0) {
      if (dryRun) {
        console.log(
          `  Would remove ${cleanedLegacyPromptShims} legacy skill prompt shim file(s).`,
        );
      } else {
        console.log(
          `  Removed ${cleanedLegacyPromptShims} legacy skill prompt shim file(s).`,
        );
      }
    }
    if (catalogCounts) {
      console.log(
        `  Prompt refresh complete (catalog baseline: ${catalogCounts.prompts}).\n`,
      );
    } else {
      console.log("  Prompt refresh complete.\n");
    }
  }