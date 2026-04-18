ask}`.slice(0, 80), description: `Review code quality and update documentation for: ${task}` },
  ];

  // Return up to workerCount aspects, repeating implementation for extra workers
  const result = aspects.slice(0, workerCount);
  while (result.length < workerCount) {
    const idx = result.length - aspects.length;
    result.push({
      subject: `Additional work (${idx + 1}): ${task}`.slice(0, 80),
      description: `Continue implementation work on: ${task}`,
    });
  }
  return result;
}