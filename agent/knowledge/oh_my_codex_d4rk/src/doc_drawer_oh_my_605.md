}).trim();
        if (tmuxSession) enableMouseScrolling(tmuxSession);
      } catch (err) {
        process.stderr.write(`[cli/index] operation failed: ${err}\n`);
        // Non-fatal: mouse scrolling is a convenience feature
      }
    }

    const activePaneId = process.env.TMUX_PANE?.trim();
    if (activePaneId) {
      try {
        execFileSync("tmux", ["display-message", "-p", "-t", activePaneId, "#S"], {
          encoding: "utf-8",
        });
      } catch {}
    }