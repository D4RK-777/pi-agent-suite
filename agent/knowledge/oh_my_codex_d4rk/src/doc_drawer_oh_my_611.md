dio =
              finalizeStep.name === "attach-session" ? "inherit" : "ignore";
            try {
              execFileSync("tmux", finalizeStep.args, { stdio });
            } catch (err) {
              process.stderr.write(`[cli/index] operation failed: ${err}\n`);
              if (finalizeStep.name === "attach-session")
                throw new Error("failed to attach detached tmux session");
              continue;
            }
            if (
              finalizeStep.name === "register-resize-hook" &&
              hookTarget &&
              hookName
            ) {
              registeredHookTarget = hookTarget;
              registeredHookName = hookName;
            }
            if (
              finalizeStep.name === "register-client-attached-reconcile" &&