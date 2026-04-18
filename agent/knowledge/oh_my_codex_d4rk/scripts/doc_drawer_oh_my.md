{
  "name": "oh-my-codex",
  "version": "0.11.12",
  "description": "Multi-agent orchestration layer for OpenAI Codex CLI",
  "type": "module",
  "main": "dist/index.js",
  "bin": {
    "omx": "dist/cli/omx.js"
  },
  "scripts": {
    "build": "node -e \"const fs=require('fs'); fs.rmSync('dist',{recursive:true,force:true});\" && tsc && node -e \"require('fs').chmodSync('dist/cli/omx.js', 0o755)\"",
    "build:explore": "cargo build -p omx-explore-harness",
    "build:full": "npm run build && npm run build:explore:release && npm run build:sparkshell",
    "build:explore:release": "node dist/scripts/build-explore-harness.js",
    "check:no-unused": "tsc -p tsconfig.no-unused.json",
    "clean:native-package-assets": "node dist/scripts/cleanup-explore-harness.js",
    "dev": "tsc --watch",