g;
      agent_count?: number;
      agent_types?: string;
    };
  } catch {
    return null;
  }
}

function resolveApprovedTeamFollowupContext(cwd: string, task: string): TeamFollowupContext | null {
  const normalizedTask = task.trim();
  if (!normalizedTask) return null;

  const existingTeamState = readPersistedTeamFollowupState(cwd);
  const shortFollowup = ['team', 'team으로 해줘', 'team으로 해주세요'].includes(normalizedTask);
  if (!shortFollowup) return null;

  const approvedHint = readApprovedExecutionLaunchHint(cwd, 'team');
  if (!approvedHint) return null;