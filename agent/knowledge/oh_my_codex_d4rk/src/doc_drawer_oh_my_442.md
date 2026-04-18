h all components.');
  } else {
    console.log('\nAll checks passed! oh-my-codex is ready.');
  }
}

interface TeamDoctorIssue {
  code: 'delayed_status_lag' | 'slow_shutdown' | 'orphan_tmux_session' | 'resume_blocker' | 'stale_leader';
  message: string;
  severity: 'warn' | 'fail';
}

async function doctorTeam(): Promise<void> {
  console.log('oh-my-codex doctor --team');
  console.log('=========================\n');

  const issues = await collectTeamDoctorIssues(process.cwd());
  if (issues.length === 0) {
    console.log('  [OK] team diagnostics: no issues');
    console.log('\nAll team checks passed.');
    return;
  }

  const failureCount = issues.filter(issue => issue.severity === 'fail').length;
  const warningCount = issues.length - failureCount;