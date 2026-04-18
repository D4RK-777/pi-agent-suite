erCase();
    if (answer === "2" || answer === "project") return "project";
    return defaultScope;
  } finally {
    rl.close();
  }
}

async function promptForModelUpgrade(
  currentModel: string,
  targetModel: string,
): Promise<boolean> {
  if (!process.stdin.isTTY || !process.stdout.isTTY) {
    return false;
  }
  const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  try {
    const answer = (
      await rl.question(
        `Detected model "${currentModel}". Update to "${targetModel}"? [Y/n]: `,
      )
    )
      .trim()
      .toLowerCase();
    return answer === "" || answer === "y" || answer === "yes";
  } finally {
    rl.close();
  }
}