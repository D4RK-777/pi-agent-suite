'fail',
          });
        }
      }
    } catch {
      // ignore malformed HUD state
    }
  }

  // orphan_tmux_session: session exists but no matching team state
  if (!tmuxUnavailable) {
    for (const session of tmuxSessions) {
      if (!knownTeamSessions.has(session)) {
        issues.push({
          code: 'orphan_tmux_session',
          message: `${session} exists without matching team state (possibly external project)`,
          severity: 'warn',
        });
      }
    }
  }

  return dedupeIssues(issues);
}