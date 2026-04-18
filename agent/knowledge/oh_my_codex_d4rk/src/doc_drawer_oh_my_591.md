name: "attach-session",
    args: ["attach-session", "-t", sessionName],
  });
  return steps;
}

export function buildDetachedSessionRollbackSteps(
  sessionName: string,
  hookTarget: string | null,
  hookName: string | null,
  clientAttachedHookName: string | null,
): DetachedSessionTmuxStep[] {
  const steps: DetachedSessionTmuxStep[] = [];
  if (hookTarget && clientAttachedHookName) {
    steps.push({
      name: "unregister-client-attached-reconcile",
      args: buildUnregisterClientAttachedReconcileArgs(
        hookTarget,
        clientAttachedHookName,
      ),
    });
  }
  if (hookTarget && hookName) {
    steps.push({
      name: "unregister-resize-hook",
      args: buildUnregisterResizeHookArgs(hookTarget, hookName),
    });
  }
  steps.push({
    name: "kill-session",