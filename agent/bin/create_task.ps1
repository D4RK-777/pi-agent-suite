# Create MemPalace Auto-Start Task
$taskName = "MemPalace_AutoStart"
$chromaScript = "$env:TEMP\chroma_autostart.py"

Write-Host "Creating MemPalace auto-start task..."

try {
    $action = New-ScheduledTaskAction -Execute "python.exe" -Argument "-X utf8 `"$chromaScript`""
    $trigger = New-ScheduledTaskTrigger -AtLogOn
    $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
    
    Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Description "MemPalace ChromaDB" -Force
    
    Write-Host "[OK] Task created successfully!"
    Write-Host ""
    Write-Host "MemPalace will start automatically when you log in."
    Write-Host ""
    
} catch {
    Write-Host "[WARN] Could not create scheduled task: $_"
    Write-Host ""
    Write-Host "Alternative: Add to Windows Startup folder:"
    Write-Host "  Win+R, shell:startup, enter"
    Write-Host "  Create shortcut to python.exe with args:"
    Write-Host "  -X utf8 $chromaScript"
}
