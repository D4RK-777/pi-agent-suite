istedSetupScope } from "./index.js";
import { isOmxGeneratedAgentsMd } from "../utils/agents-md.js";

export interface UninstallOptions {
  dryRun?: boolean;
  keepConfig?: boolean;
  verbose?: boolean;
  purge?: boolean;
  scope?: SetupScope;
}

interface UninstallSummary {
  configCleaned: boolean;
  mcpServersRemoved: string[];
  agentEntriesRemoved: number;
  tuiSectionRemoved: boolean;
  topLevelKeysRemoved: boolean;
  featureFlagsRemoved: boolean;
  promptsRemoved: number;
  skillsRemoved: number;
  agentConfigsRemoved: number;
  agentsMdRemoved: boolean;
  cacheDirectoryRemoved: boolean;
}

const OMX_MCP_SERVERS = [
  "omx_state",
  "omx_memory",
  "omx_code_intel",
  "omx_trace",
];