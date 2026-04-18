#!/usr/bin/env bash
# D4rk Mind — Start Knowledge Daemons
# Runs all knowledge agents in the background

set -e

BIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="$HOME/.mempalace/logs"
PID_DIR="$HOME/.mempalace/pids"

# Create directories
mkdir -p "$LOG_DIR" "$PID_DIR"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║           D4rk Mind — Starting Knowledge Daemons         ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Function to start a daemon
start_daemon() {
    local name=$1
    local cmd=$2
    local log_file="$LOG_DIR/${name}.log"
    local pid_file="$PID_DIR/${name}.pid"
    
    # Check if already running
    if [ -f "$pid_file" ]; then
        local pid=$(cat "$pid_file")
        if kill -0 "$pid" 2>/dev/null; then
            echo "  ✓ ${name} already running (PID: $pid)"
            return 0
        fi
    fi
    
    echo "  Starting ${name}..."
    cd "$BIN_DIR"
    
    # Start in background
    nohup $cmd > "$log_file" 2>&1 &
    local pid=$!
    
    # Save PID
    echo $pid > "$pid_file"
    
    # Wait a moment for startup
    sleep 2
    
    # Verify it's running
    if kill -0 "$pid" 2>/dev/null; then
        echo "  ✓ ${name} started (PID: $pid)"
    else
        echo "  ✗ ${name} failed to start"
        echo "    Check: tail -f $log_file"
    fi
}

# Function to stop a daemon
stop_daemon() {
    local name=$1
    local pid_file="$PID_DIR/${name}.pid"
    
    if [ -f "$pid_file" ]; then
        local pid=$(cat "$pid_file")
        if kill -0 "$pid" 2>/dev/null; then
            echo "  Stopping ${name} (PID: $pid)..."
            kill "$pid" 2>/dev/null || true
            sleep 1
        fi
        rm -f "$pid_file"
    fi
}

# Parse command
CMD=${1:-start}

case "$CMD" in
    start)
        echo "Starting daemons..."
        echo ""
        
        # Start knowledge gardener
        start_daemon "knowledge_gardener" \
            "python -X utf8 ${BIN_DIR}/knowledge_gardener.py --daemon --interval 86400"
        
        # Start mine agent
        start_daemon "mine_agent" \
            "python -X utf8 ${BIN_DIR}/mine_agent.py --watch --daemon"
        
        echo ""
        echo "════════════════════════════════════════════════════════════════"
        echo ""
        echo "All daemons started!"
        echo ""
        echo "Logs:"
        echo "  tail -f ~/.mempalace/logs/knowledge_gardener.log"
        echo "  tail -f ~/.mempalace/logs/mine_agent.log"
        echo ""
        echo "Status:"
        echo "  ls ~/.mempalace/pids/"
        echo ""
        echo "Stop:"
        echo "  bash ${BIN_DIR}/start_daemons.sh stop"
        echo ""
        ;;
        
    stop)
        echo "Stopping daemons..."
        echo ""
        
        stop_daemon "knowledge_gardener"
        stop_daemon "mine_agent"
        
        echo ""
        echo "All daemons stopped."
        ;;
        
    status)
        echo "Daemon Status:"
        echo ""
        
        for pid_file in "$PID_DIR"/*.pid; do
            if [ -f "$pid_file" ]; then
                name=$(basename "$pid_file" .pid)
                pid=$(cat "$pid_file")
                
                if kill -0 "$pid" 2>/dev/null; then
                    echo "  ✓ ${name}: running (PID: $pid)"
                else
                    echo "  ✗ ${name}: not running (stale PID file)"
                fi
            fi
        done
        
        echo ""
        ;;
        
    restart)
        echo "Restarting daemons..."
        echo ""
        bash "$0" stop
        sleep 2
        bash "$0" start
        ;;
        
    *)
        echo "Usage: $0 {start|stop|status|restart}"
        exit 1
        ;;
esac
