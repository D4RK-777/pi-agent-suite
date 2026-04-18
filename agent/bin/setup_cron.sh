#!/usr/bin/env bash
# Setup cron jobs for continuous codebase mining

set -e

INSTALL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="python"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║           D4rk Mind — Cron Setup                           ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Detect platform
case "$(uname -s)" in
    Linux*)     PLATFORM=linux;;
    Darwin*)    PLATFORM=macos;;
    CYGWIN*|MINGW*|MSYS*) PLATFORM=windows;;
    *)          PLATFORM=unknown;;
esac

echo "Platform: $PLATFORM"
echo ""

# Create cron entry for hourly mining
CRON_CMD="cd $INSTALL_DIR && $PYTHON mine_agent.py --watch --interval=3600"

# Detect existing cron entries
CRON_EXISTING=$(crontab -l 2>/dev/null | grep -c "mine_agent.py" || true)

if [ "$CRON_EXISTING" -gt 0 ]; then
    echo "⚠️  mine_agent already in crontab"
    echo ""
    echo "Existing entries:"
    crontab -l | grep mine_agent
    echo ""
    read -p "Remove and reinstall? (y/N) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        crontab -l | grep -v mine_agent | crontab -
        echo "Removed old entries."
    else
        echo "Keeping existing entries."
        exit 0
    fi
fi

# Add new cron entry
if [ "$PLATFORM" = "windows" ]; then
    echo "⚠️  Cron not available on Windows"
    echo ""
    echo "Use the daemon mode instead:"
    echo "  python mine_agent.py --watch --daemon"
    echo ""
    echo "Or use Windows Task Scheduler:"
    echo "  taskschd.msc"
    exit 1
fi

# Create cron entry
(crontab -l 2>/dev/null || true; echo "0 * * * * cd $INSTALL_DIR && $PYTHON mine_agent.py >> /tmp/mine_agent.log 2>&1") | crontab -

echo "✅ Cron job installed!"
echo ""
echo "Current crontab:"
crontab -l
echo ""

# Also offer to start daemon now
echo ""
read -p "Start the mining daemon now? (Y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    cd "$INSTALL_DIR"
    echo "Starting daemon in background..."
    nohup $PYTHON mine_agent.py --watch --daemon > /tmp/mine_agent_daemon.log 2>&1 &
    echo "✅ Daemon started! (PID: $!)"
    echo ""
    echo "View logs: tail -f /tmp/mine_agent.log"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                    Setup Complete                            ║"
echo "╠════════════════════════════════════════════════════════════════╣"
echo "║                                                              ║"
echo "║  Cron job: Every hour, mines all codebases                  ║"
echo "║  Daemon:   Continuous watching with --watch                ║"
echo "║                                                              ║"
echo "║  Commands:                                                 ║"
echo "║    python mine_agent.py --watch          # Watch mode      ║"
echo "║    python mine_agent.py --watch --daemon # Background      ║"
echo "║    python mine_agent.py --auto-detect    # All projects    ║"
echo "║    crontab -e                            # Edit cron      ║"
echo "║                                                              ║"
echo "╚════════════════════════════════════════════════════════════════╝"
