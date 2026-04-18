}
            if (
              finalizeStep.name === "register-client-attached-reconcile" &&
              clientAttachedHookName
            ) {
              registeredClientAttachedHookName = clientAttachedHookName;
            }
          }
        }
      }
    } catch (err) {
      process.stderr.write(`[cli/index] operation failed: ${err}\n`);
      if (createdDetachedSession) {
        const rollbackSteps = buildDetachedSessionRollbackSteps(
          sessionName,
          registeredHookTarget,
          registeredHookName,
          registeredClientAttachedHookName,
        );
        for (const rollbackStep of rollbackSteps) {
          try {
            execFileSync("tmux", rollbackStep.args, { stdio: "ignore" });
          } catch (err) {