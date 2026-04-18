dowIndex = hudPaneId
            ? detectDetachedSessionWindowIndex(sessionName)
            : null;
          const hookTarget =
            hudPaneId && hookWindowIndex
              ? buildResizeHookTarget(sessionName, hookWindowIndex)
              : null;
          const hookName =
            hudPaneId && hookWindowIndex
              ? buildResizeHookName(
                  "launch",
                  sessionName,
                  hookWindowIndex,
                  hudPaneId,
                )
              : null;
          const clientAttachedHookName =
            hudPaneId && hookWindowIndex
              ? buildClientAttachedReconcileHookName(
                  "launch",
                  sessionName,
                  hookWindowIndex,
                  hudPaneId,