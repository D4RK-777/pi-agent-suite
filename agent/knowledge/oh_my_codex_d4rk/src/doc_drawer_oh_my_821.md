om '../team/leader-activity.js';

type TeamWorkerCli = Exclude<WorkerInfo['worker_cli'], undefined>;

interface TeamCliOptions {
  verbose?: boolean;
}

interface ParsedTeamArgs {
  workerCount: number;
  agentType: string;
  explicitAgentType: boolean;
  explicitWorkerCount: boolean;
  task: string;
  teamName: string;
}


interface TeamFollowupContext {
  task: string;
  workerCount: number;
  explicitWorkerCount: boolean;
  agentType?: string;
  explicitAgentType?: boolean;
}