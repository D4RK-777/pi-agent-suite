#!/usr/bin/env node
/**
 * Pi Agent Suite — npm CLI entry point
 *
 * Usage:
 *   pi-agent-suite install     # run the interactive installer
 *   pi-agent-suite verify      # run verification checks
 *   pi-agent-suite check-python  # check Python >= 3.9 is available
 */

const { execSync, spawnSync } = require("child_process");
const path = require("path");
const fs = require("fs");
const os = require("os");

const SUITE_DIR = path.join(__dirname, "..");
const command = process.argv[2] || "help";

function checkPython() {
  for (const bin of ["python3", "python"]) {
    try {
      const result = spawnSync(bin, ["-c", "import sys; print(sys.version_info.major, sys.version_info.minor)"], {
        encoding: "utf8",
        timeout: 5000,
      });
      if (result.status === 0) {
        const [maj, min] = result.stdout.trim().split(" ").map(Number);
        if (maj > 3 || (maj === 3 && min >= 9)) {
          console.log(`[OK] Python ${maj}.${min} found (${bin})`);
          return bin;
        }
        console.warn(`[!] ${bin} is ${maj}.${min} — need 3.9+`);
      }
    } catch {
      // try next
    }
  }
  console.error("[x] Python 3.9+ not found. Install from https://python.org");
  return null;
}

function runInstaller() {
  const isWindows = process.platform === "win32";

  if (isWindows) {
    const script = path.join(SUITE_DIR, "installer", "install.ps1");
    console.log("Running Windows installer...");
    const result = spawnSync("powershell", ["-ExecutionPolicy", "Bypass", "-File", script], {
      stdio: "inherit",
      timeout: 300000,
    });
    process.exit(result.status ?? 1);
  } else {
    const script = path.join(SUITE_DIR, "installer", "install.sh");
    fs.chmodSync(script, "755");
    console.log("Running bash installer...");
    const result = spawnSync("bash", [script], {
      stdio: "inherit",
      timeout: 300000,
    });
    process.exit(result.status ?? 1);
  }
}

function runVerify() {
  const script = path.join(SUITE_DIR, "installer", "verify.sh");
  if (process.platform === "win32") {
    console.log("Running verify.sh via bash...");
    const result = spawnSync("bash", [script], { stdio: "inherit", timeout: 60000 });
    process.exit(result.status ?? 1);
  } else {
    fs.chmodSync(script, "755");
    const result = spawnSync("bash", [script], { stdio: "inherit", timeout: 60000 });
    process.exit(result.status ?? 1);
  }
}

function showHelp() {
  console.log(`
Pi Agent Suite — CLI

Commands:
  install       Run the interactive installer (MemPalace + harness + hooks)
  verify        Run verification checks
  check-python  Check Python 3.9+ availability
  help          Show this help

Examples:
  npx pi-agent-suite install
  npx pi-agent-suite verify
`);
}

switch (command) {
  case "install":
    runInstaller();
    break;
  case "verify":
    runVerify();
    break;
  case "check-python":
    process.exit(checkPython() ? 0 : 1);
    break;
  case "help":
  default:
    showHelp();
}
