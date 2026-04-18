,
        sessionName: session.ok && session.stdout ? session.stdout : undefined,
      };
    }
  }

  const currentClientPane = runTmux(['display-message', '-p', '#{pane_id}']);
  if (currentClientPane.ok && currentClientPane.stdout) {
    const session = runTmux(['display-message', '-p', '#S']);
    return {
      target: { type: 'pane', value: currentClientPane.stdout },
      sessionName: session.ok && session.stdout ? session.stdout : undefined,
    };
  }

  const activePane = detectActivePaneFromList();
  if (activePane) return activePane;