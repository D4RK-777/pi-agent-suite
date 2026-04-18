k.js";
import { cleanupCommand } from "./cleanup.js";
import { exploreCommand } from "./explore.js";
import { sparkshellCommand } from "./sparkshell.js";
import { agentsInitCommand } from "./agents-init.js";
import { agentsCommand } from "./agents.js";
import { sessionCommand } from "./session-search.js";
import { autoresearchCommand } from "./autoresearch.js";
import {
  MADMAX_FLAG,
  CODEX_BYPASS_FLAG,
  HIGH_REASONING_FLAG,
  XHIGH_REASONING_FLAG,
  SPARK_FLAG,
  MADMAX_SPARK_FLAG,
  CONFIG_FLAG,
  LONG_CONFIG_FLAG,
} from "./constants.js";
import {
  getBaseStateDir,
  getStateDir,
  listModeStateFilesWithScopePreference,
} from "../mcp/state-paths.js";
import { maybeCheckAndPromptUpdate } from "./update.js";
import { maybePromptGithubStar } from "./star-prompt.js";
import {