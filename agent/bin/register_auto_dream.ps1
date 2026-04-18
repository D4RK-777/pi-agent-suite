# Register a Windows Scheduled Task to run auto_dream.py nightly at 02:15.
#
# Run this ONCE from an elevated PowerShell:
#     powershell -ExecutionPolicy Bypass -File ${PI_AGENT_HOME}\agent\bin\register_auto_dream.ps1
#
# To unregister:
#     Unregister-ScheduledTask -TaskName "pi-auto-dream" -Confirm:$false

$taskName = "pi-auto-dream"
$script = "${PI_AGENT_HOME}\agent\bin\auto_dream.py"
$pythonw = "pythonw"

# Use pythonw so no console window flashes.
$action = New-ScheduledTaskAction -Execute $pythonw -Argument "-X utf8 `"$script`""

# 02:15 daily - well after typical session activity.
$trigger = New-ScheduledTaskTrigger -Daily -At 2:15AM

# Run as the current user, only when logged on (no need for service-level rights).
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 15)

# Replace any prior registration.
Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue | Out-Null

Register-ScheduledTask `
    -TaskName $taskName `
    -Description "pi Auto-Dream: nightly memory consolidation report" `
    -Action $action `
    -Trigger $trigger `
    -Principal $principal `
    -Settings $settings | Out-Null

Write-Host "Registered scheduled task '$taskName' - runs daily at 02:15."
Write-Host "Reports land in: ~\.pi\sessions\reports\auto-dream-YYYY-MM-DD.md"
Write-Host ""
Write-Host "Run once now to verify:"
Write-Host "    Start-ScheduledTask -TaskName '$taskName'"
