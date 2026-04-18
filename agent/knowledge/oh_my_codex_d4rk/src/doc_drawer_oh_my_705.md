from "../config/generator.js";
import {
  getUnifiedMcpRegistryCandidates,
  loadUnifiedMcpRegistry,
  planClaudeCodeMcpSettingsSync,
  type UnifiedMcpRegistryLoadResult,
} from "../config/mcp-registry.js";
import { generateAgentToml } from "../agents/native-config.js";
import { AGENT_DEFINITIONS } from "../agents/definitions.js";
import { getPackageRoot } from "../utils/package.js";
import { readSessionState, isSessionStale } from "../hooks/session.js";
import { getCatalogHeadlineCounts } from "./catalog-contract.js";
import { tryReadCatalogManifest } from "../catalog/reader.js";
import { DEFAULT_FRONTIER_MODEL } from "../config/models.js";
import {
  addGeneratedAgentsMarker,
  isOmxGeneratedAgentsMd,
} from "../utils/agents-md.js";
import {
  resolveAgentsModelTableContext,