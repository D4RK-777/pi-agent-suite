isOmxGeneratedAgentsMd,
} from "../utils/agents-md.js";
import {
  resolveAgentsModelTableContext,
  upsertAgentsModelTable,
} from "../utils/agents-model-table.js";
import { spawnPlatformCommandSync } from "../utils/platform-command.js";

interface SetupOptions {
  codexVersionProbe?: () => string | null;
  force?: boolean;
  dryRun?: boolean;
  scope?: SetupScope;
  verbose?: boolean;
  agentsOverwritePrompt?: (destinationPath: string) => Promise<boolean>;
  modelUpgradePrompt?: (
    currentModel: string,
    targetModel: string,
  ) => Promise<boolean>;
  mcpRegistryCandidates?: string[];
}