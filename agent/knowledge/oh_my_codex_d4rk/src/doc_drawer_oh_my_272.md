import { existsSync } from "node:fs";
import {
  mkdir,
  readdir,
  readFile,
  stat,
  writeFile,
  copyFile,
} from "node:fs/promises";
import { basename, dirname, join, relative, resolve } from "node:path";
import { getPackageRoot } from "../utils/package.js";
import { readSessionState, isSessionStale } from "../hooks/session.js";

export const AGENTS_INIT_USAGE = [
  "Usage: omx agents-init [path] [--dry-run] [--force] [--verbose]",
  "       omx deepinit [path] [--dry-run] [--force] [--verbose]",
  "",
  "Bootstrap lightweight AGENTS.md files for the target directory and its direct child directories.",
  "",
  "Options:",
  "  --dry-run   Show planned file updates without writing files",
  "  --force     Overwrite existing unmanaged AGENTS.md files after taking a backup",