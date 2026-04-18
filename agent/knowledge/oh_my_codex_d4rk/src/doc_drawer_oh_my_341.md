mptAction(io, deepInterview.launchReady);
      if (action === 'refine') {
        continue;
      }

      return materializeAutoresearchDeepInterviewResult(deepInterview);
    }
  } finally {
    io.close();
  }
}

export async function guidedAutoresearchSetup(repoRoot: string): Promise<InitAutoresearchResult> {
  return runAutoresearchNoviceBridge(repoRoot);
}

export function checkTmuxAvailable(): boolean {
  const result = spawnSync('tmux', ['-V'], { stdio: 'pipe',
      windowsHide: true,
    });
  return result.status === 0;
}

export function spawnAutoresearchTmux(missionDir: string, slug: string): void {
  if (!checkTmuxAvailable()) {
    throw new Error('tmux is required for background autoresearch execution. Install tmux and try again.');
  }