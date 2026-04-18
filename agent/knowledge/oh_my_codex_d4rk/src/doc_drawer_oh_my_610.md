nch",
                  sessionName,
                  hookWindowIndex,
                  hudPaneId,
                )
              : null;
          const finalizeSteps = buildDetachedSessionFinalizeSteps(
            sessionName,
            hudPaneId,
            hookWindowIndex,
            process.env.OMX_MOUSE !== "0",
            nativeWindows,
          );
          if (nativeWindows && detachedWindowsCodexCmd) {
            scheduleDetachedWindowsCodexLaunch(
              sessionName,
              detachedWindowsCodexCmd,
            );
          }
          for (const finalizeStep of finalizeSteps) {
            const stdio =
              finalizeStep.name === "attach-session" ? "inherit" : "ignore";
            try {