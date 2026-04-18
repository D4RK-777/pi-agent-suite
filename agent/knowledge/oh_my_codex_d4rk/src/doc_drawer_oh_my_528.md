INDOWS_DETACHED_BOOTSTRAP_DELAY_MS = 2500;
const CODEX_VERSION_FLAGS = new Set(["--version", "-V"]);

type CliCommand =
  | "launch"
  | "exec"
  | "setup"
  | "agents"
  | "agents-init"
  | "deepinit"
  | "uninstall"
  | "doctor"
  | "cleanup"
  | "ask"
  | "explore"
  | "sparkshell"
  | "team"
  | "session"
  | "resume"
  | "version"
  | "tmux-hook"
  | "hooks"
  | "hud"
  | "status"
  | "cancel"
  | "help"
  | "reasoning"
  | string;

const NESTED_HELP_COMMANDS = new Set<CliCommand>([
  "ask",
  "cleanup",
  "autoresearch",
  "agents",
  "agents-init",
  "deepinit",
  "exec",
  "hooks",
  "hud",
  "ralph",
  "resume",
  "session",
  "sparkshell",
  "team",
  "tmux-hook",
]);

export interface ResolvedCliInvocation {
  command: CliCommand;
  launchArgs: string[];
}