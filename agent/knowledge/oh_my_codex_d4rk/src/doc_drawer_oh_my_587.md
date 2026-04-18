, args: newSessionArgs },
    { name: "split-and-capture-hud-pane", args: splitCaptureArgs },
  ];
}

async function readLaunchAppendInstructions(): Promise<string> {
  const appendixCandidates = [
    process.env[OMX_RALPH_APPEND_INSTRUCTIONS_FILE_ENV]?.trim(),
    process.env[OMX_AUTORESEARCH_APPEND_INSTRUCTIONS_FILE_ENV]?.trim(),
  ].filter(
    (value): value is string => typeof value === "string" && value.length > 0,
  );
  if (appendixCandidates.length === 0) return "";
  const appendixPath = appendixCandidates[0];
  if (!existsSync(appendixPath)) {
    throw new Error(`launch instructions file not found: ${appendixPath}`);
  }
  const { readFile } = await import("fs/promises");
  return (await readFile(appendixPath, "utf-8")).trim();
}