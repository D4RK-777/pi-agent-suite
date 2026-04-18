# Pi Universal Harness Launcher
#
# Usage from ANY AI:
#   powershell -ExecutionPolicy Bypass -File "$env:PI_AGENT_HOME\pi-harness.ps1" <command> [args]
#
# After install the path is ~/.pi/pi-harness.ps1 (or $env:PI_AGENT_HOME\pi-harness.ps1)
#
# Commands:
#   search <query>              - Search MemPalace
#   context <query> [wing]     - Get memory context for agent
#   route <task>               - Route to best agent
#   plan <task>                - Multi-agent plan
#   stats                       - Memory statistics
#   info                        - System info
#   help                        - Show this help

param(
    [Parameter(Position=0)]
    [string]$Command = "help",

    [Parameter(Position=1)]
    [string]$Arg1 = "",

    [Parameter(Position=2)]
    [string]$Arg2 = ""
)

$ErrorActionPreference = "Continue"
# Resolve install root: env var wins, fall back to ~/.pi
$PI_ROOT = if ($env:PI_AGENT_HOME) { $env:PI_AGENT_HOME } else { Join-Path $HOME ".pi" }
$HARNESS_DIR = Join-Path $PI_ROOT "agent\harness"
$MEMORY_BIN  = Join-Path $PI_ROOT "agent\bin"

function Show-Help {
    Write-Host @"
═══════════════════════════════════════════════════════════════════
  🧠 Pi Universal Harness
═══════════════════════════════════════════════════════════════════

  Central harness for all AI agents. Use MemPalace + routing.

  MEMORY (MemPalace):
    search <query>           - Search patterns (22ms recall)
    context <query> [wing]  - Get agent context
    stats                   - Memory statistics

  ROUTING:
    route <task>            - Route to best agent
    plan <task>             - Multi-agent plan

  QUALITY:
    gate                    - Quality gate
    test                    - Run routing tests

  EXAMPLES:
    . pi-harness.ps1 search "react hooks patterns"
    . pi-harness.ps1 context "jwt auth" frontend
    . pi-harness.ps1 route "build login form"
    . pi-harness.ps1 plan "full-stack feature"

═══════════════════════════════════════════════════════════════════
"@
}

function Invoke-PythonHarness {
    param($cmd, $args)
    $pythonArgs = @("-m", "harness", $cmd) + $args
    Push-Location (Join-Path $PI_ROOT "agent")
    try {
        python @pythonArgs
    } finally {
        Pop-Location
    }
}

function Invoke-MemorySearch {
    param($query, $wing)
    
    $searchScript = @"
import sys
sys.path.insert(0, r'$MEMORY_BIN')
from mempalace_fast import search
import json

results = search('$query', n=5)
print(json.dumps(results, indent=2))
"@
    
    $results = python -X utf8 -c $searchScript 2>&1
    return $results
}

# ═══════════════════════════════════════════════════════════════════
# MAIN DISPATCH
# ═══════════════════════════════════════════════════════════════════

switch ($Command.ToLower()) {
    "help" {
        Show-Help
    }
    
    # Memory commands
    "search" {
        if ([string]::IsNullOrEmpty($Arg1)) {
            Write-Host "Usage: pi-harness.ps1 search <query>"
            exit 1
        }
        $results = Invoke-MemorySearch -query $Arg1 -wing $null
        Write-Host $results
    }
    
    "context" {
        if ([string]::IsNullOrEmpty($Arg1)) {
            Write-Host "Usage: pi-harness.ps1 context <query> [wing]"
            exit 1
        }
        
        $query = $Arg1
        $wing = if ([string]::IsNullOrEmpty($Arg2)) { $null } else { $Arg2 }
        
        $searchScript = @"
import sys
sys.path.insert(0, r'$MEMORY_BIN')
from mempalace_fast import search
import json

results = search('$query', n=3)

# Format for agent context
for r in results.get('results', []):
    print(f"## From: {r.get('source', 'unknown')}")
    content = r.get('content', '')[:500]
    print(content)
    print()
"@
        
        python -X utf8 -c $searchScript
    }
    
    "stats" {
        $statsScript = @"
import sys
sys.path.insert(0, r'$MEMORY_BIN')
from mempalace_fast import get_stats
import json

try:
    stats = get_stats()
    print(json.dumps(stats, indent=2))
except:
    # Fallback to CLI
    import subprocess
    result = subprocess.run(['python', '-X', 'utf8', '-m', 'mempalace.cli', 'status'], 
                          capture_output=True, text=True)
    print(result.stdout)
"@
        
        python -X utf8 -c $statsScript
    }
    
    # Harness commands
    "route" {
        if ([string]::IsNullOrEmpty($Arg1)) {
            Write-Host "Usage: pi-harness.ps1 route <task>"
            exit 1
        }
        Invoke-PythonHarness -cmd "route" -args @($Arg1)
    }
    
    "plan" {
        if ([string]::IsNullOrEmpty($Arg1)) {
            Write-Host "Usage: pi-harness.ps1 plan <task>"
            exit 1
        }
        Invoke-PythonHarness -cmd "plan" -args @($Arg1)
    }
    
    "gate" {
        Invoke-PythonHarness -cmd "gate" -args @()
    }
    
    "test" {
        Invoke-PythonHarness -cmd "test" -args @()
    }
    
    "info" {
        Invoke-PythonHarness -cmd "info" -args @()
    }
    
    default {
        Write-Host "Unknown command: $Command"
        Write-Host ""
        Show-Help
        exit 1
    }
}
