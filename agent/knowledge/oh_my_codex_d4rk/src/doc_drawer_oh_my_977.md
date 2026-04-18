snapshot.performance.worker_scan_ms} mailbox=${snapshot.performance.mailbox_delivery_ms}`
    );
  }
  for (const hint of buildLeaderMonitoringHints(runtime.teamName)) {
    console.log(hint);
  }
}

export function buildLeaderMonitoringHints(teamName: string): string[] {
  const sanitized = sanitizeTeamName(teamName);
  return [
    `leader_check: omx team status ${sanitized}`,
    `leader_loop_hint: while ON, keep checking state (example: sleep 30 && omx team status ${sanitized})`,
  ];
}