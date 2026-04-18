= `
Usage: omx team api <operation> [--input <json>] [--json]
       omx team api <operation> --help

Supported operations:
  ${TEAM_API_OPERATIONS.join('\n  ')}

Examples:
  omx team api list-tasks --input '{"team_name":"my-team"}' --json
  omx team api claim-task --input '{"team_name":"my-team","task_id":"1","worker":"worker-1","expected_version":1}' --json
`;

const HELP_TOKENS = new Set(['--help', '-h', 'help']);