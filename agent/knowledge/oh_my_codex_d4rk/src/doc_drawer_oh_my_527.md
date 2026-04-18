ARCH_APPEND_INSTRUCTIONS_FILE";
const REASONING_MODES = ["low", "medium", "high", "xhigh"] as const;
type ReasoningMode = (typeof REASONING_MODES)[number];
const REASONING_MODE_SET = new Set<string>(REASONING_MODES);
const REASONING_USAGE = "Usage: omx reasoning <low|medium|high|xhigh>";
const ALLOWED_SHELLS = new Set([
  "/bin/sh",
  "/bin/bash",
  "/bin/zsh",
  "/bin/dash",
  "/bin/fish",
  "/usr/bin/sh",
  "/usr/bin/bash",
  "/usr/bin/zsh",
  "/usr/bin/dash",
  "/usr/bin/fish",
  "/usr/local/bin/bash",
  "/usr/local/bin/zsh",
  "/usr/local/bin/fish",
]);
const WINDOWS_DETACHED_BOOTSTRAP_DELAY_MS = 2500;
const CODEX_VERSION_FLAGS = new Set(["--version", "-V"]);