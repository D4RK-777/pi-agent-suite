es.js dist",
    "test:compat:node": "npm run build && node --test dist/compat/__tests__/*.test.js",
    "test:compat:node:cross-platform": "npm run build && node dist/scripts/run-test-files.js dist/compat/__tests__",
    "test:compat:rust": "cargo build && OMX_COMPAT_TARGET=./target/debug/omx npm run test:compat:node",
    "build:sparkshell": "node dist/scripts/build-sparkshell.js",
    "smoke:packed-install": "node dist/scripts/smoke-packed-install.js",
    "test:sparkshell": "node dist/scripts/test-sparkshell.js",
    "test:reply-listener:live": "node dist/scripts/test-reply-listener-live.js",
    "postpack": "npm run clean:native-package-assets"
  },
  "engines": {
    "node": ">=20"
  },
  "files": [
    "Cargo.toml",
    "Cargo.lock",
    "dist/",
    "crates/",
    "agents/",