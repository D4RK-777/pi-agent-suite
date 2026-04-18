execFileSync("tmux", rollbackStep.args, { stdio: "ignore" });
          } catch (err) {
            process.stderr.write(`[cli/index] operation failed: ${err}\n`);
            // best-effort rollback only
          }
        }
      }
      // tmux not available or failed, just run codex directly
      runCodexBlocking(cwd, launchArgs, codexEnvWithNotify);
    }
  }
}

function listHudWatchPaneIdsInCurrentWindow(currentPaneId?: string): string[] {
  try {
    const output = execFileSync(
      "tmux",
      [
        "list-panes",
        "-F",
        "#{pane_id}\t#{pane_current_command}\t#{pane_start_command}",
      ],
      { encoding: "utf-8" },
    );
    return findHudWatchPaneIds(parseTmuxPaneSnapshot(output), currentPaneId);
  } catch (err) {