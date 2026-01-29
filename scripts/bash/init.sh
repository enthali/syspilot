#!/bin/bash
# syspilot Bootstrap Script (Linux/Mac)
# 
# This script copies the Setup Agent to your project and configures VS Code.
# Run this once to bootstrap syspilot in your project.
#
# Usage: ./init.sh
#

set -e

# Find syspilot root (where this script lives)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SYSPILOT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROJECT_ROOT="$(pwd)"

echo "syspilot Bootstrap"
echo "=================="
echo ""
echo "syspilot location: $SYSPILOT_ROOT"
echo "Project location:  $PROJECT_ROOT"
echo ""

# Check if we're in the syspilot directory itself
if [ "$SYSPILOT_ROOT" = "$PROJECT_ROOT" ]; then
    echo "[ERROR] Cannot install syspilot into itself!"
    echo "        Please run this script from your project directory."
    echo ""
    echo "Example:"
    echo "  cd /path/to/your/project"
    echo "  /path/to/syspilot/scripts/bash/init.sh"
    exit 1
fi

# Create .github/agents directory if it doesn't exist
AGENTS_DIR="$PROJECT_ROOT/.github/agents"
if [ ! -d "$AGENTS_DIR" ]; then
    echo "Creating .github/agents directory..."
    mkdir -p "$AGENTS_DIR"
fi

# Copy the Setup Agent
SETUP_AGENT_SOURCE="$SYSPILOT_ROOT/agents/syspilot.setup.agent.md"
SETUP_AGENT_DEST="$AGENTS_DIR/syspilot.setup.agent.md"

if [ -f "$SETUP_AGENT_SOURCE" ]; then
    echo "Copying Setup Agent..."
    cp "$SETUP_AGENT_SOURCE" "$SETUP_AGENT_DEST"
    echo "  -> $SETUP_AGENT_DEST"
else
    echo "[WARN] Setup Agent not found at: $SETUP_AGENT_SOURCE"
    echo "       Creating minimal Setup Agent..."
    
    cat > "$SETUP_AGENT_DEST" << 'EOF'
---
description: Install and update syspilot in this project.
---

# syspilot Setup Agent

I will help you install or update syspilot in this project.

Please provide the path to your syspilot installation directory.
EOF
fi

# Update or create .vscode/settings.json
VSCODE_DIR="$PROJECT_ROOT/.vscode"
SETTINGS_FILE="$VSCODE_DIR/settings.json"

if [ ! -d "$VSCODE_DIR" ]; then
    echo "Creating .vscode directory..."
    mkdir -p "$VSCODE_DIR"
fi

if [ -f "$SETTINGS_FILE" ]; then
    echo "Updating VS Code settings..."
    # Use Python to merge JSON (more reliable than jq which may not be installed)
    python3 -c "
import json
import sys

try:
    with open('$SETTINGS_FILE', 'r') as f:
        settings = json.load(f)
except:
    settings = {}

if 'chat.promptFilesRecommendations' not in settings:
    settings['chat.promptFilesRecommendations'] = {}
settings['chat.promptFilesRecommendations']['syspilot.setup'] = True

with open('$SETTINGS_FILE', 'w') as f:
    json.dump(settings, f, indent=4)
" 2>/dev/null || {
    echo "[WARN] Could not update settings.json with Python, creating new one"
    echo '{"chat.promptFilesRecommendations":{"syspilot.setup":true}}' > "$SETTINGS_FILE"
}
else
    echo "Creating VS Code settings..."
    echo '{"chat.promptFilesRecommendations":{"syspilot.setup":true}}' > "$SETTINGS_FILE"
fi

echo ""
echo "[OK] Bootstrap complete!"
echo ""
echo "Next steps:"
echo "1. Open this project in VS Code"
echo "2. Open Copilot Chat (Ctrl+Shift+I)"
echo "3. Type: @syspilot.setup"
echo "4. Follow the Setup Agent's instructions"
echo ""
