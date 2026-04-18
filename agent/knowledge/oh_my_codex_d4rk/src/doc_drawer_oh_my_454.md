oject)`,
          severity: 'warn',
        });
      }
    }
  }

  return dedupeIssues(issues);
}

function dedupeIssues(issues: TeamDoctorIssue[]): TeamDoctorIssue[] {
  const seen = new Set<string>();
  const out: TeamDoctorIssue[] = [];
  for (const issue of issues) {
    const key = `${issue.code}:${issue.message}`;
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(issue);
  }
  return out;
}

function listTeamTmuxSessions(): Set<string> | null {
  const { result: res } = spawnPlatformCommandSync('tmux', ['list-sessions', '-F', '#{session_name}'], { encoding: 'utf-8' });
  if (res.error) {
    // tmux binary unavailable or not executable.
    return null;
  }