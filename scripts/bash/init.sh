#!/bin/bash
# syspilot Bootstrap Script (Linux/Mac)
# 
# Copies the Setup Agent to your project. That's it.
# The Setup Agent handles everything else interactively.
#
# Usage: /path/to/syspilot/scripts/bash/init.sh
#

set -e

# Find syspilot root (2 levels up from this script)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SYSPILOT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PROJECT_ROOT="$(pwd)"

# Don't install into syspilot itself
if [ "$SYSPILOT_ROOT" = "$PROJECT_ROOT" ]; then
    echo "Run this from your project directory, not from syspilot."
    exit 1
fi

# Create .github/agents and copy Setup Agent
mkdir -p "$PROJECT_ROOT/.github/agents"
cp "$SYSPILOT_ROOT/.github/agents/syspilot.setup.agent.md" "$PROJECT_ROOT/.github/agents/"

echo "Done. Open VS Code, start GitHub Copilot Chat, and select @syspilot.setup"
