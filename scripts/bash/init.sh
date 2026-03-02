#!/bin/bash
# syspilot Bootstrap Script (Linux/Mac)
#
# Downloads the Setup Agent to your project via curl. That's it.
# The Setup Agent handles everything else interactively.
#
# Usage: curl -sL https://raw.githubusercontent.com/enthali/syspilot/main/scripts/bash/init.sh | bash
#    or: bash /path/to/syspilot/scripts/bash/init.sh
#

set -e

mkdir -p .github/agents
curl -fsSL \
  "https://raw.githubusercontent.com/enthali/syspilot/main/.github/agents/syspilot.setup.agent.md" \
  -o .github/agents/syspilot.setup.agent.md

echo "Done. Open VS Code, start GitHub Copilot Chat, and select @syspilot.setup"
