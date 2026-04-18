ctionsFile;
    } else {
      delete process.env[AUTORESEARCH_APPEND_INSTRUCTIONS_ENV];
    }
  }
}

function checkTmuxAvailable(): boolean {
  const result = spawnSync('tmux', ['-V'], { stdio: 'pipe',
      windowsHide: true,
    });
  return result.status === 0;
}

function tmuxDisplay(target: string, format: string): string | null {
  const result = spawnSync('tmux', ['display-message', '-p', '-t', target, format], { encoding: 'utf-8',
      windowsHide: true,
    });
  if (result.error || result.status !== 0) return null;
  const value = (result.stdout || '').trim();
  return value || null;
}