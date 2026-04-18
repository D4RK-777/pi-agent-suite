/**
 * oh-my-codex CLI
 * Multi-agent orchestration for OpenAI Codex CLI
 */

import { execFileSync, spawn } from "child_process";
import { basename, dirname, join } from "path";
import { existsSync, readFileSync } from "fs";
import { constants as osConstants } from "os";
import { setup, SETUP_SCOPES, type SetupScope } from "./setup.js";
import { uninstall } from "./uninstall.js";
import { version } from "./version.js";
import { tmuxHookCommand } from "./tmux-hook.js";
import { hooksCommand } from "./hooks.js";
import { hudCommand } from "../hud/index.js";
import { teamCommand } from "./team.js";
import { ralphCommand } from "./ralph.js";
import { askCommand } from "./ask.js";
import { cleanupCommand } from "./cleanup.js";
import { exploreCommand } from "./explore.js";