console.error(`[omx] failed to launch codex: ${errno.message}`);
    }
    throw result.error;
  }

  if (result.status !== 0) {
    process.exitCode =
      typeof result.status === "number"
        ? result.status
        : resolveSignalExitCode(result.signal);
    if (result.signal) {
      console.error(`[omx] codex exited due to signal ${result.signal}`);
    }
  }
}

interface TmuxPaneSnapshot {
  paneId: string;
  currentCommand: string;
  startCommand: string;
}

export interface DetachedSessionTmuxStep {
  name: string;
  args: string[];
}