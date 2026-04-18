# Setup ChromaDB as a Windows Startup Task
# Run this once to make ChromaDB start automatically on login

$taskName = "MemPalace_ChromaDB"
$scriptPath = Join-Path $PSScriptRoot "start_chroma_server.ps1"

# Remove existing task if present
$existing = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existing) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
    Write-Host "Removed existing task: $taskName"
}

# Create action - run PowerShell
$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-ExecutionPolicy Bypass -WindowStyle Hidden -File `"$scriptPath`""

# Create trigger - at logon
$trigger = New-ScheduledTaskTrigger `
    -AtLogOn

# Create principal - run as current user
$principal = New-ScheduledTaskPrincipal `
    -UserId $env:USERNAME `
    -LogonType Interactive `
    -RunLevel Limited

# Create settings
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -RunOnlyIfNetworkAvailable:$false

# Register the task
Register-ScheduledTask `
    -TaskName $taskName `
    -Action $action `
    -Trigger $trigger `
    -Principal $principal `
    -Settings $settings `
    -Description "MemPalace ChromaDB vector database server"

Write-Host ""
Write-Host "Scheduled Task Created: $taskName"
Write-Host "ChromaDB will start automatically when you log in."
Write-Host ""
Write-Host "To start now without waiting for logon:"
Write-Host "  powershell -ExecutionPolicy Bypass -File `"$scriptPath`""
Write-Host ""
Write-Host "To check if running:"
Write-Host "  Get-Process python | Where-Object { `$_.CommandLine -like '*chromadb*' }"
Write-Host ""
Write-Host "To remove:"
Write-Host "  Unregister-ScheduledTask -TaskName $taskName -Confirm:`$false"
