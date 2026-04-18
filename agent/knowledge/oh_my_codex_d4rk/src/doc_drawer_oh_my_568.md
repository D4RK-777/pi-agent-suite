return resolveTeamLowComplexityDefaultModel(codexHomeOverride);
    }
  }
  return undefined;
}

function isModelInstructionsOverride(value: string): boolean {
  return new RegExp(`^${MODEL_INSTRUCTIONS_FILE_KEY}\\s*=`).test(value.trim());
}

function hasModelInstructionsOverride(args: string[]): boolean {
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg === CONFIG_FLAG || arg === LONG_CONFIG_FLAG) {
      const maybeValue = args[i + 1];
      if (
        typeof maybeValue === "string" &&
        isModelInstructionsOverride(maybeValue)
      ) {
        return true;
      }
      continue;
    }