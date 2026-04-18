, paneId] : null;
      })
      .filter((entry): entry is [string, string] => entry !== null),
  );

  const sparkshellCommands = Object.fromEntries(
    [
      leaderPaneId ? ['leader', `omx sparkshell --tmux-pane ${leaderPaneId} --tail-lines ${tailLines}`] : null,
      hudPaneId ? ['hud', `omx sparkshell --tmux-pane ${hudPaneId} --tail-lines ${tailLines}`] : null,
      ...Object.entries(workerPanes).map(([workerName, paneId]) => [
        workerName,
        `omx sparkshell --tmux-pane ${paneId} --tail-lines ${tailLines}`,
      ] as const),
    ].filter((entry): entry is [string, string] => entry !== null),
  );