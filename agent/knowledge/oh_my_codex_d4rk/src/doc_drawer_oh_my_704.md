/**
 * omx setup - Automated installation of oh-my-codex
 * Installs skills, prompts, MCP servers config, and AGENTS.md
 */

import {
  mkdir,
  copyFile,
  readdir,
  readFile,
  writeFile,
  stat,
  rm,
} from "fs/promises";
import { join, dirname, relative } from "path";
import { existsSync } from "fs";
import { spawnSync } from "child_process";
import { createInterface } from "readline/promises";
import { homedir } from "os";
import {
  codexHome,
  codexConfigPath,
  codexPromptsDir,
  codexAgentsDir,
  userSkillsDir,
  omxStateDir,
  detectLegacySkillRootOverlap,
  omxPlansDir,
  omxLogsDir,
} from "../utils/paths.js";
import { buildMergedConfig, getRootModelName } from "../config/generator.js";
import {
  getUnifiedMcpRegistryCandidates,
  loadUnifiedMcpRegistry,