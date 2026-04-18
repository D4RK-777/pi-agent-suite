mode: opts.mode,
  });
  await dispatchHookEvent(payload, {
    cwd,
    enabled: true,
  });
}

function notifyFallbackPidPath(cwd: string): string {
  return join(cwd, ".omx", "state", "notify-fallback.pid");
}

function hookDerivedWatcherPidPath(cwd: string): string {
  return join(cwd, ".omx", "state", "hook-derived-watcher.pid");
}

function parseWatcherPidFile(content: string): number | null {
  const trimmed = content.trim();
  if (!trimmed) return null;
  try {
    const parsed = JSON.parse(trimmed) as { pid?: unknown };
    return typeof parsed.pid === "number" &&
      Number.isFinite(parsed.pid) &&
      parsed.pid > 0
      ? parsed.pid
      : null;
  } catch {
    const pid = Number.parseInt(trimmed, 10);
    return Number.isFinite(pid) && pid > 0 ? pid : null;
  }
}