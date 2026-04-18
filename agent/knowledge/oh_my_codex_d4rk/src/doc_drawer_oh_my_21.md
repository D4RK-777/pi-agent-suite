/**
 * Native agent config generators for Codex CLI.
 * Writes standalone TOML files under ~/.codex/agents/ or ./.codex/agents/.
 */

import { existsSync, readFileSync } from "fs";
import { mkdir, readFile, writeFile } from "fs/promises";
import { join } from "path";
import { AGENT_DEFINITIONS, AgentDefinition } from "./definitions.js";
import {
  getEnvConfiguredStandardDefaultModel,
  getMainDefaultModel,
  getSparkDefaultModel,
  getStandardDefaultModel,
} from "../config/models.js";
import { getRootModelName } from "../config/generator.js";
import { codexAgentsDir } from "../utils/paths.js";

export const EXACT_GPT_5_4_MINI_MODEL = "gpt-5.4-mini";