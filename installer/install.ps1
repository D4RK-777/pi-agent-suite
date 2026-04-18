# Pi Agent Suite — Windows PowerShell Installer
# Run with: powershell -ExecutionPolicy Bypass -File installer/install.ps1

param(
    [string]$PiHome = "",
    [string]$Palace = "",
    [switch]$NonInteractive,
    [switch]$NoClaude,
    [switch]$WithVault
)

$ErrorActionPreference = "Stop"

# ─── Helpers ──────────────────────────────────────────────────────────────────
function Write-Ok($msg)   { Write-Host "  [OK] $msg" -ForegroundColor Green }
function Write-Info($msg) { Write-Host "  [i]  $msg" -ForegroundColor Cyan }
function Write-Warn($msg) { Write-Host "  [!]  $msg" -ForegroundColor Yellow }
function Write-Die($msg)  { Write-Host "  [x]  $msg" -ForegroundColor Red; exit 1 }

# ─── Defaults ─────────────────────────────────────────────────────────────────
$DefaultPiHome = if ($env:PI_AGENT_HOME) { $env:PI_AGENT_HOME } else { Join-Path $HOME ".pi" }
$DefaultPalace = if ($env:MEMPALACE_PALACE) { $env:MEMPALACE_PALACE } else { Join-Path $HOME ".mempalace\palace" }

if (-not $PiHome) { $PiHome = $DefaultPiHome }
if (-not $Palace) { $Palace = $DefaultPalace }
$PatchClaude = -not $NoClaude

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SuiteDir  = Split-Path -Parent $ScriptDir

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor White
Write-Host "  Pi Agent Suite — Windows Installer" -ForegroundColor White
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor White
Write-Host ""

# ─── Interactive prompts ──────────────────────────────────────────────────────
if (-not $NonInteractive) {
    $inp = Read-Host "Install directory [$PiHome]"
    if ($inp) { $PiHome = $inp }

    $inp = Read-Host "MemPalace data directory [$Palace]"
    if ($inp) { $Palace = $inp }

    $inp = Read-Host "Patch Claude Code settings.json? [Y/n]"
    if ($inp -match "^[Nn]") { $PatchClaude = $false }

    $inp = Read-Host "Set up Obsidian vault template? [y/N]"
    if ($inp -match "^[Yy]") { $WithVault = $true }
    Write-Host ""
}

# ─── Prerequisites ────────────────────────────────────────────────────────────
Write-Info "Checking prerequisites..."

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command python3 -ErrorAction SilentlyContinue
}
if (-not $python) { Write-Die "Python 3.9+ required. Download from python.org." }

$pyver = & $python.Source -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
$pymaj, $pymin = $pyver -split "\."
if ([int]$pymaj -lt 3 -or ([int]$pymaj -eq 3 -and [int]$pymin -lt 9)) {
    Write-Die "Python 3.9+ required (found $pyver)."
}
Write-Ok "Python $pyver"
$PYTHON = $python.Source

# ─── Install MemPalace ────────────────────────────────────────────────────────
Write-Host ""
Write-Info "Installing MemPalace..."

$mp_check = & $PYTHON -c "import mempalace; print(mempalace.__version__)" 2>$null
if ($LASTEXITCODE -eq 0 -and $mp_check) {
    Write-Ok "MemPalace already installed ($mp_check)"
} else {
    & $PYTHON -m pip install mempalace --quiet
    if ($LASTEXITCODE -ne 0) { Write-Die "pip install mempalace failed." }
    $mp_check = & $PYTHON -c "import mempalace; print(mempalace.__version__)" 2>$null
    Write-Ok "MemPalace $mp_check installed"
}

# ─── Create directory structure ───────────────────────────────────────────────
Write-Host ""
Write-Info "Creating Pi Agent directory at $PiHome..."

@(
    "$PiHome\agent\bin",
    "$PiHome\agent\harness",
    "$PiHome\agent\agents",
    "$PiHome\agent\manifests",
    "$PiHome\agent\skills",
    "$PiHome\agent\adapters",
    "$PiHome\hooks"
) | ForEach-Object { New-Item -ItemType Directory -Path $_ -Force | Out-Null }

$HookStateDir = Join-Path (Split-Path $Palace -Parent) "hook_state"
New-Item -ItemType Directory -Path $HookStateDir -Force | Out-Null
Write-Ok "Directories created"

# ─── Copy harness files ───────────────────────────────────────────────────────
Write-Info "Installing Pi Agent engine (harness, agents, manifests, adapters, bin)..."
Copy-Item "$SuiteDir\agent\*" "$PiHome\agent\" -Recurse -Force
Write-Ok "Agent engine installed"

Write-Info "Installing hook scripts..."
Copy-Item "$SuiteDir\hooks\*" "$PiHome\hooks\" -Force
Write-Ok "Hook scripts"

# ─── Write env file ───────────────────────────────────────────────────────────
$EnvFile = Join-Path $PiHome "env.ps1"
@"
# Pi Agent Suite — environment variables
# Dot-source this in your PowerShell profile: . "$EnvFile"

`$env:PI_AGENT_HOME = "$PiHome"
`$env:MEMPALACE_PALACE = "$Palace"

# Uncomment to point at your Obsidian vault:
# `$env:OBSIDIAN_VAULT = "C:\path\to\your\vault"
# `$env:OBSIDIAN_API_KEY = "your-key-here"
"@ | Set-Content $EnvFile -Encoding UTF8
Write-Ok "Env file written to $EnvFile"

$ProfileFile = $PROFILE.CurrentUserAllHosts
if ($ProfileFile -and -not (Select-String -Path $ProfileFile -Pattern "PI_AGENT_HOME" -Quiet -ErrorAction SilentlyContinue)) {
    "`n# Pi Agent Suite`n. `"$EnvFile`"" | Add-Content $ProfileFile
    Write-Ok "Added env to $ProfileFile"
}

# ─── Pi launcher batch file ───────────────────────────────────────────────────
$PiBat = Join-Path $PiHome "pi.bat"
@"
@echo off
python "$PiHome\agent\harness\orchestrator.py" %*
"@ | Set-Content $PiBat -Encoding ASCII
Write-Ok "Created pi.bat launcher at $PiBat"

# ─── Patch Claude Code settings ───────────────────────────────────────────────
if ($PatchClaude) {
    Write-Host ""
    Write-Info "Wiring up Claude Code hooks and MCP server..."

    $ClaudeDir = Join-Path $env:APPDATA "Claude"
    if (-not (Test-Path $ClaudeDir)) { $ClaudeDir = Join-Path $HOME ".claude" }

    $SettingsPath = Join-Path $ClaudeDir "settings.json"
    $SettingsLocalPath = Join-Path $ClaudeDir "settings.local.json"

    $TargetSettings = if (Test-Path $SettingsPath) {
        Write-Warn "settings.json exists — writing hooks to settings.local.json instead"
        $SettingsLocalPath
    } else {
        $SettingsPath
    }

    $HookPrompt  = "python `"$PiHome\agent\bin\mempalace_prompt_hook.py`""
    $HookStop    = "bash `"$PiHome\hooks\mempal_save_hook.sh`""
    $HookCompact = "bash `"$PiHome\hooks\mempal_precompact_hook.sh`""

    $patchScript = @"
import json, sys
from pathlib import Path

target = Path(r"$TargetSettings")
data = {}
if target.exists():
    try:
        data = json.loads(target.read_text(encoding='utf-8'))
    except Exception:
        data = {}

hooks = data.setdefault('hooks', {})

def set_hook(event, cmd, timeout=2):
    hooks.setdefault(event, [])
    for entry in hooks[event]:
        for h in entry.get('hooks', []):
            if h.get('command', '').startswith(cmd.split()[0]):
                return
    hooks[event].append({'matcher': '', 'hooks': [{'type': 'command', 'command': cmd, 'timeout': timeout}]})

set_hook('UserPromptSubmit', r'$HookPrompt', 2)
set_hook('Stop', r'$HookStop', 30)
set_hook('PreCompact', r'$HookCompact', 30)

mcp = data.setdefault('mcpServers', {})
if 'mempalace' not in mcp:
    mcp['mempalace'] = {
        'command': 'python',
        'args': ['-m', 'mempalace.mcp_server', '--palace', r'$Palace'],
    }

target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(data, indent=2), encoding='utf-8')
print(f'Wrote {target}')
"@
    & $PYTHON -c $patchScript
    Write-Ok "Claude Code hooks and MCP server configured"
}

# ─── Vault template ───────────────────────────────────────────────────────────
if ($WithVault) {
    Write-Host ""
    $VaultPath = Read-Host "Obsidian vault path (will be created)"
    if (-not (Test-Path $VaultPath)) {
        Copy-Item "$SuiteDir\vault-template" $VaultPath -Recurse
        Write-Ok "Vault created at $VaultPath"
    } else {
        Copy-Item "$SuiteDir\vault-template\*" $VaultPath -Recurse -Force
        Write-Ok "Vault template copied to $VaultPath"
    }

    Write-Host ""
    Write-Info "Next steps for Obsidian:"
    Write-Info "1. Open Obsidian -> Add vault -> $VaultPath"
    Write-Info "2. Install 'Local REST API' community plugin"
    Write-Info "3. Copy the API key into $EnvFile (OBSIDIAN_API_KEY)"
}

# ─── Palace check ─────────────────────────────────────────────────────────────
Write-Host ""
Write-Info "Checking MemPalace..."
& $PYTHON "$PiHome\agent\bin\mempalace_fast.py"

# ─── Done ─────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Green
Write-Host "  Installation complete!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Reload PowerShell (or run: . `"$ProfileFile`")"
Write-Host "  2. Mine a project:    mempalace mine C:\path\to\your-project"
Write-Host "  3. Test the harness:  python -m harness route 'build a login form'"
Write-Host "  4. Open Claude Code — hooks fire automatically"
Write-Host ""
