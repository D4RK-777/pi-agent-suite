/**
 * omx uninstall - Remove oh-my-codex configuration and installed artifacts
 */

import { readFile, writeFile, readdir, rm } from "fs/promises";
import { existsSync } from "fs";
import { join, basename } from "path";
import {
  stripExistingOmxBlocks,
  stripOmxEnvSettings,
  stripOmxTopLevelKeys,
  stripOmxFeatureFlags,
} from "../config/generator.js";
import { getPackageRoot } from "../utils/package.js";
import { AGENT_DEFINITIONS } from "../agents/definitions.js";
import { resolveScopeDirectories, type SetupScope } from "./setup.js";
import { readPersistedSetupScope } from "./index.js";
import { isOmxGeneratedAgentsMd } from "../utils/agents-md.js";