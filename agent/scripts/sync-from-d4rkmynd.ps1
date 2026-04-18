# Pi Skill Sync Script
# Syncs skills from a canonical skill source into the Pi harness.
# Useful if you maintain skills in a separate vault or shared location
# and want to link (not copy) them into the Pi skills directory.
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File "$env:PI_AGENT_HOME\agent\scripts\sync-from-d4rkmynd.ps1"
#   powershell -ExecutionPolicy Bypass -File "..." -SourceRoot "D:\MyVault"

param(
    [string]$SourceRoot = "",
    [string]$TargetRoot = ""
)

$ErrorActionPreference = "Stop"

$PiHome = if ($env:PI_AGENT_HOME) { $env:PI_AGENT_HOME } else { Join-Path $env:USERPROFILE ".pi" }

if (-not $SourceRoot) { $SourceRoot = Join-Path $PiHome "skills-canonical" }
if (-not $TargetRoot) { $TargetRoot = Join-Path $PiHome "agent\skills" }

$SourceManifest = Join-Path $SourceRoot "skills.json"

if (-not (Test-Path $SourceRoot)) {
    Write-Host "[INFO] No canonical skill source found at: $SourceRoot" -ForegroundColor Yellow
    Write-Host "[INFO] Set -SourceRoot to your skill source directory." -ForegroundColor Yellow
    Write-Host "[INFO] Skills already bundled in $TargetRoot are unaffected." -ForegroundColor Cyan
    exit 0
}

if (-not (Test-Path $SourceManifest)) {
    Write-Host "[ERROR] No skills.json manifest found at: $SourceManifest" -ForegroundColor Red
    exit 1
}

$manifest = Get-Content -LiteralPath $SourceManifest -Raw | ConvertFrom-Json
$canonicalSkills = @(
    $manifest.skills |
    Where-Object { $_.status -eq "active" } |
    ForEach-Object { $_.name }
)

Write-Host "========================================"
Write-Host "  Pi Skill Sync"
Write-Host "========================================"
Write-Host ""
Write-Host "Source:           $SourceRoot"
Write-Host "Target:           $TargetRoot"
Write-Host "Active skills:    $($canonicalSkills.Count)"
Write-Host ""

$synced = 0; $skipped = 0; $failed = 0

foreach ($skill in $canonicalSkills) {
    $source = Join-Path $SourceRoot $skill
    $dest   = Join-Path $TargetRoot $skill

    if (-not (Test-Path $source)) {
        Write-Host "  [SKIP] Source not found: $skill" -ForegroundColor DarkGray
        $skipped++
        continue
    }

    try {
        if (Test-Path $dest) {
            $backup = "$dest.bak"
            if (Test-Path $backup) { Remove-Item $backup -Recurse -Force }
            Move-Item $dest $backup
            Write-Host "  [MOVE] $skill (backed up)" -ForegroundColor Yellow
        }

        $null = New-Item -ItemType Junction -Path $dest -Target $source -Force
        Write-Host "  [LINK] $skill" -ForegroundColor Green
        $synced++
    }
    catch {
        Write-Host "  [FAIL] $skill : $_" -ForegroundColor Red
        $failed++
    }
}

Write-Host ""
Write-Host "========================================"
Write-Host "  Sync Complete: $synced linked, $skipped skipped, $failed failed"
Write-Host "========================================"
Write-Host ""
