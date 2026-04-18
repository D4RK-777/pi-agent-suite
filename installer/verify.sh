#!/usr/bin/env bash
# Pi Agent Suite — Post-install verification
# Usage: bash installer/verify.sh

set -uo pipefail

PI_HOME="${PI_AGENT_HOME:-$HOME/.pi}"
PALACE="${MEMPALACE_PALACE:-$HOME/.mempalace/palace}"

pass=0; fail=0

check() {
    local label="$1"; local cmd="$2"
    if eval "$cmd" >/dev/null 2>&1; then
        echo "  [OK] $label"
        ((pass++))
    else
        echo "  [FAIL] $label"
        ((fail++))
    fi
}

echo ""
echo "Pi Agent Suite — Verification"
echo "─────────────────────────────"
check "Python 3.9+"      "python3 -c 'import sys; sys.exit(0 if sys.version_info>=(3,9) else 1)'"
check "MemPalace package" "python3 -c 'import mempalace'"
check "ChromaDB package"  "python3 -c 'import chromadb'"
check "Harness engine"    "test -f '$PI_HOME/agent/harness/router.py'"
check "Bin scripts"       "test -f '$PI_HOME/agent/bin/mempalace_fast.py'"
check "Hook: save"        "test -f '$PI_HOME/hooks/mempal_save_hook.sh'"
check "Hook: precompact"  "test -f '$PI_HOME/hooks/mempal_precompact_hook.sh'"
check "Manifests"         "test -f '$PI_HOME/agent/manifests/agents.json'"
check "Palace data dir"   "test -d '$PALACE' || python3 -m mempalace status 2>/dev/null"
check "mempalace_fast"    "python3 '$PI_HOME/agent/bin/mempalace_fast.py'"
check "Harness routing"   "python3 -m harness route 'build a login form' 2>/dev/null"

echo ""
echo "─────────────────────────────"
echo "  Passed: $pass  Failed: $fail"

if [[ $fail -gt 0 ]]; then
    echo ""
    echo "Run: bash installer/install.sh to fix missing components."
    echo "See: docs/01-installation.md for manual steps."
    exit 1
else
    echo ""
    echo "All checks passed. Pi Agent Suite is ready."
fi
