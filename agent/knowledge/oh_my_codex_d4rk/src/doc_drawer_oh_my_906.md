hs[target] ?? null,
        team_manifest_path: recommendedInspectTeamManifestPaths[target] ?? null,
        team_events_path: recommendedInspectTeamEventsPaths[target] ?? null,
        team_dispatch_path: recommendedInspectTeamDispatchPaths[target] ?? null,
        team_phase_path: recommendedInspectTeamPhasePaths[target] ?? null,
        team_monitor_snapshot_path: recommendedInspectTeamMonitorSnapshotPaths[target] ?? null,
        team_summary_snapshot_path: recommendedInspectTeamSummarySnapshotPaths[target] ?? null,
        command,
      };
    })
    .filter((item): item is Exclude<typeof item, null> => item !== null);