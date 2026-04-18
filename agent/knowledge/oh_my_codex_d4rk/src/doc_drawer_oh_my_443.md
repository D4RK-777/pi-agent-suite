ter(issue => issue.severity === 'fail').length;
  const warningCount = issues.length - failureCount;

  for (const issue of issues) {
    const icon = issue.severity === 'warn' ? '[!!]' : '[XX]';
    console.log(`  ${icon} ${issue.code}: ${issue.message}`);
  }

  console.log(`\nResults: ${warningCount} warnings, ${failureCount} failed`);
  // Ensure non-zero exit for `omx doctor --team` failures.
  if (failureCount > 0) process.exitCode = 1;
}

async function collectTeamDoctorIssues(cwd: string): Promise<TeamDoctorIssue[]> {
  const issues: TeamDoctorIssue[] = [];
  const stateDir = omxStateDir(cwd);
  const teamsRoot = join(stateDir, 'team');
  const nowMs = Date.now();
  const lagThresholdMs = 60_000;
  const shutdownThresholdMs = 30_000;
  const leaderStaleThresholdMs = 180_000;