riting files",
  "  --force     Overwrite existing unmanaged AGENTS.md files after taking a backup",
  "  --verbose   Print per-file actions and skip reasons",
  "  --help      Show this message",
].join("\n");

const MANAGED_MARKER = "<!-- OMX:AGENTS-INIT:MANAGED -->";
const MANUAL_START = "<!-- OMX:AGENTS-INIT:MANUAL:START -->";
const MANUAL_END = "<!-- OMX:AGENTS-INIT:MANUAL:END -->";
const DEFAULT_LIST_LIMIT = 12;
const IGNORE_DIRECTORY_NAMES = new Set([
  ".git",
  ".omx",
  ".codex",
  "node_modules",
  "dist",
  "build",
  "coverage",
  ".next",
  ".nuxt",
  ".turbo",
  ".cache",
  "__pycache__",
  "vendor",
  "target",
  "tmp",
  "temp",
]);

interface AgentsInitOptions {
  dryRun?: boolean;
  force?: boolean;
  verbose?: boolean;
  targetPath?: string;
}