readFile } = await import("fs/promises");
  return (await readFile(appendixPath, "utf-8")).trim();
}

export function buildDetachedSessionFinalizeSteps(
  sessionName: string,
  hudPaneId: string | null,
  hookWindowIndex: string | null,
  enableMouse: boolean,
  nativeWindows = false,
): DetachedSessionTmuxStep[] {
  const steps: DetachedSessionTmuxStep[] = [];
  if (!nativeWindows && hudPaneId && hookWindowIndex) {
    const hookTarget = buildResizeHookTarget(sessionName, hookWindowIndex);
    const hookName = buildResizeHookName(
      "launch",
      sessionName,
      hookWindowIndex,
      hudPaneId,
    );
    const clientAttachedHookName = buildClientAttachedReconcileHookName(
      "launch",
      sessionName,
      hookWindowIndex,
      hudPaneId,
    );
    steps.push({