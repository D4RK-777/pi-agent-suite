body: string;
}

export interface AutoresearchEvaluatorResult {
  pass: boolean;
  score?: number;
}

export interface AutoresearchMissionContract {
  missionDir: string;
  repoRoot: string;
  missionFile: string;
  sandboxFile: string;
  missionRelativeDir: string;
  missionContent: string;
  sandboxContent: string;
  sandbox: ParsedSandboxContract;
  missionSlug: string;
}

const MISSION_DIR_GIT_ERROR = 'mission-dir must be inside a git repository.';
const SANDBOX_FRONTMATTER_ERROR = 'sandbox.md must start with YAML frontmatter containing evaluator.command and evaluator.format=json.';
const EVALUATOR_BLOCK_ERROR = 'sandbox.md frontmatter must define an evaluator block.';
const EVALUATOR_COMMAND_ERROR = 'sandbox.md frontmatter evaluator.command is required.';