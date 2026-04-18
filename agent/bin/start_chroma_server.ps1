# ChromaDB Server Launcher
# Keeps ChromaDB running permanently with persistent storage
# For Windows Task Scheduler or manual launch

param(
    [string]$Port = "8000",
    [string]$DataPath = "$env:USERPROFILE\.mempalace\palace",
    [switch]$AutoRestart
)

$ErrorActionPreference = "Stop"

# Paths
$LogDir = "$env:USERPROFILE\.mempalace\logs"
$PidDir = "$env:USERPROFILE\.mempalace\pids"
$LogFile = "$LogDir\chroma_server.log"
$PidFile = "$PidDir\chroma_server.pid"

# Ensure directories exist
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
New-Item -ItemType Directory -Force -Path $PidDir | Out-Null

# Check if already running
if (Test-Path $PidFile) {
    $existingPid = Get-Content $PidFile -ErrorAction SilentlyContinue
    if ($existingPid -and (Get-Process -Id $existingPid -ErrorAction SilentlyContinue)) {
        Write-Host "ChromaDB server already running (PID: $existingPid)"
        exit 0
    }
    Remove-Item $PidFile -Force
}

Write-Host "Starting ChromaDB server..."
Write-Host "  Port: $Port"
Write-Host "  Data: $DataPath"
Write-Host "  Logs: $LogFile"
Write-Host ""

# Start ChromaDB with persistent storage
# --persist-directory ensures data survives restarts
# --allow-reset allows resetting the database if needed

$env:CHROMA_SERVER_NO_AUTH = "1"  # Local-only, no auth needed

$process = Start-Process `
    -FilePath "python" `
    -ArgumentList "-X utf8 -m chromadb --port $Port --persist-directory `"$DataPath`" --allow-reset" `
    -WindowStyle Hidden `
    -PassThru `
    -RedirectStandardOutput $LogFile `
    -RedirectStandardError "$LogDir\chroma_server_error.log"

# Save PID
$process.Id | Set-Content $PidFile

# Wait for startup
Start-Sleep -Seconds 3

# Verify it's running
if ($process.HasExited) {
    Write-Host "ERROR: ChromaDB failed to start"
    Write-Host "Check logs: $LogFile"
    exit 1
}

Write-Host "ChromaDB started successfully (PID: $($process.Id))"
Write-Host "API available at: http://localhost:$Port"
Write-Host ""

# Auto-restart loop if requested
if ($AutoRestart) {
    Write-Host "Auto-restart enabled. Monitoring for crashes..."
    while (-not $process.HasExited) {
        Start-Sleep -Seconds 5
    }
    
    Write-Host "ChromaDB crashed. Restarting in 5 seconds..."
    Start-Sleep -Seconds 5
    & $MyInvocation.MyCommand.Path -Port $Port -DataPath $DataPath -AutoRestart
}

# Cleanup on normal exit
$process.WaitForExit()
Remove-Item $PidFile -Force -ErrorAction SilentlyContinue
