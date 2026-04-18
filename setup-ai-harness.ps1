param([string]$AI = "")

# Resolve install root: env var wins, fall back to ~/.pi
$PI_ROOT = if ($env:PI_AGENT_HOME) { $env:PI_AGENT_HOME } else { Join-Path $env:USERPROFILE ".pi" }
$HOME = $env:USERPROFILE

function Write-Step($msg) {
    Write-Host "  [OK] $msg" -ForegroundColor Green
}

function Setup-ClaudeCode {
    Write-Host "Setting up Claude Code..." -ForegroundColor Yellow
    $cmdDir = "$HOME\.claude\commands"
    New-Item -ItemType Directory -Path $cmdDir -Force | Out-Null
    $content = "# Memory Search`n# Usage: /memory <query>`n`nWrite-Host 'Searching Pi MemPalace...'`n`n`$query = `$args -join ' '`n& powershell -ExecutionPolicy Bypass -File '$PI_ROOT\pi-harness.ps1' search `$query"
    $content | Out-File "$cmdDir\memory.md" -Encoding UTF8
    Write-Step "Created /memory command"
}

function Setup-Codex {
    Write-Host "Setting up Codex..." -ForegroundColor Yellow
    $skDir = "$HOME\.codex\skills"
    New-Item -ItemType Directory -Path $skDir -Force | Out-Null
    $content = "# Pi Harness for Codex`nSearch Pi MemPalace before coding.`n`npowershell -ExecutionPolicy Bypass -File '$PI_ROOT\pi-harness.ps1' search 'query'"
    $content | Out-File "$skDir\pi-harness.md" -Encoding UTF8
    Write-Step "Created pi-harness.md"
}

function Setup-Qwen {
    Write-Host "Setting up Qwen..." -ForegroundColor Yellow
    $skDir = "$HOME\.qwen\skills"
    New-Item -ItemType Directory -Path $skDir -Force | Out-Null
    $content = "# Pi Harness for Qwen`npowershell -ExecutionPolicy Bypass -File '$PI_ROOT\pi-harness.ps1' search 'query'"
    $content | Out-File "$skDir\pi-harness.md" -Encoding UTF8
    Write-Step "Created pi-harness.md"
}

function Setup-Cline {
    Write-Host "Setting up Cline..." -ForegroundColor Yellow
    $skDir = "$HOME\.cline\skills"
    New-Item -ItemType Directory -Path $skDir -Force | Out-Null
    $content = "# Pi Harness for Cline`npowershell -ExecutionPolicy Bypass -File '$PI_ROOT\pi-harness.ps1' search 'query'"
    $content | Out-File "$skDir\pi-harness.md" -Encoding UTF8
    Write-Step "Created pi-harness.md"
}

function Setup-Cursor {
    Write-Host "Setting up Cursor..." -ForegroundColor Yellow
    $f = "$HOME\.cursor\.cursorrules"
    $ref = "============================================================`nPI HARNESS`npowershell -ExecutionPolicy Bypass -File '$PI_ROOT\pi-harness.ps1' search 'task'`n============================================================"
    if (Test-Path $f) { Add-Content $f $ref } else { $ref | Out-File $f -Encoding UTF8 }
    Write-Step "Updated .cursorrules"
}

function Setup-Windsurf {
    Write-Host "Setting up Windsurf..." -ForegroundColor Yellow
    $f = "$HOME\.windsurfrules"
    $ref = "============================================================`nPI HARNESS`npowershell -ExecutionPolicy Bypass -File '$PI_ROOT\pi-harness.ps1' search 'task'`n============================================================"
    if (Test-Path $f) { Add-Content $f $ref } else { $ref | Out-File $f -Encoding UTF8 }
    Write-Step "Updated .windsurfrules"
}

Write-Host ""
Write-Host "Pi Harness Setup" -ForegroundColor Cyan
Write-Host ""

if ($AI -eq "" -or $AI.ToLower() -eq "all") {
    Setup-ClaudeCode; Setup-Codex; Setup-Qwen; Setup-Cline; Setup-Cursor; Setup-Windsurf
} else {
    switch ($AI.ToLower()) {
        "claude" { Setup-ClaudeCode }
        "codex" { Setup-Codex }
        "qwen" { Setup-Qwen }
        "cline" { Setup-Cline }
        "cursor" { Setup-Cursor }
        "windsurf" { Setup-Windsurf }
    }
}
Write-Host ""
Write-Host "Done!" -ForegroundColor Green
