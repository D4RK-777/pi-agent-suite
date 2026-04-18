# Install MemPalace keeper as the Windows login auto-start entry.
#
# What this does:
#   1. Finds existing MemPalace_Daemon.lnk in the user's Startup folder.
#   2. Rewrites its target to launch mempalace_keeper.py (not the daemon directly).
#   3. The keeper then spawns the daemon and respawns it if it dies.
#
# Run once, with:  powershell -ExecutionPolicy Bypass -File install_keeper_autostart.ps1
#
# Re-run is safe — it just updates the shortcut in place.

$ErrorActionPreference = "Stop"

$StartupDir = [Environment]::GetFolderPath("Startup")
$DaemonLnk = Join-Path $StartupDir "MemPalace_Daemon.lnk"
$PythonW = "C:\Python313\pythonw.exe"
$KeeperScript = "${PI_AGENT_HOME}\agent\bin\mempalace_keeper.py"

if (-not (Test-Path $PythonW)) {
    Write-Error "pythonw.exe not found at $PythonW. Update script with correct path."
    exit 1
}
if (-not (Test-Path $KeeperScript)) {
    Write-Error "keeper script not found at $KeeperScript."
    exit 1
}

$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($DaemonLnk)
$Shortcut.TargetPath = $PythonW
$Shortcut.Arguments = "`"$KeeperScript`""
$Shortcut.WorkingDirectory = Split-Path $KeeperScript -Parent
$Shortcut.Description = "MemPalace keeper - launches daemon and auto-restarts on failure"
$Shortcut.WindowStyle = 7  # minimized (pythonw already hides console, but be explicit)
$Shortcut.Save()

Write-Host "OK - $DaemonLnk now launches $KeeperScript via pythonw"
Write-Host ""
Write-Host "To activate without reboot, run:"
Write-Host "  Stop-Process -Name pythonw -Force    # kills daemon + any old keeper"
Write-Host "  Start-Process '$DaemonLnk'           # launch the new keeper"
