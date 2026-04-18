rtCommand: string;
}

export interface DetachedSessionTmuxStep {
  name: string;
  args: string[];
}

export function parseTmuxPaneSnapshot(output: string): TmuxPaneSnapshot[] {
  return output
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line) => {
      const [paneId = "", currentCommand = "", ...startCommandParts] =
        line.split("\t");
      return {
        paneId: paneId.trim(),
        currentCommand: currentCommand.trim(),
        startCommand: startCommandParts.join("\t").trim(),
      };
    })
    .filter((pane) => pane.paneId.startsWith("%"));
}