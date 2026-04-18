"[omx]   winget install psmux\n" +
            "[omx] See: https://github.com/marlocarlo/psmux",
        );
      } else {
        console.warn(
          `[omx] warning: tmux probe failed on native Windows (${errno.code || errno.message}). Continuing without tmux/HUD.`,
        );
      }
    } else if (result.status !== 0 && !isTmuxAvailable()) {
      const stderr = (result.stderr || "").trim();
      console.warn(
        `[omx] warning: tmux reported an error on native Windows${stderr ? ` (${stderr})` : ""}. Continuing without tmux/HUD.`,
      );
    }
  }