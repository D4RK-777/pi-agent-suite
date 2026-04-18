;
    case 'reviewer': return 'leader-fixed';
    case 'decision_reason': return 'approved in demo';
    case 'required': return true;
    default: return `<${field}>`;
  }
}

function buildTeamApiOperationHelp(operation: TeamApiOperation): string {
  const requiredFields = TEAM_API_OPERATION_REQUIRED_FIELDS[operation] ?? [];
  const optionalFields = TEAM_API_OPERATION_OPTIONAL_FIELDS[operation] ?? [];
  const sampleInput: Record<string, unknown> = {};