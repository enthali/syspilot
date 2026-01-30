# syspilot Bootstrap Script (Windows)
# 
# Copies the Setup Agent to your project. That's it.
# The Setup Agent handles everything else interactively.
#
# Usage: C:\path\to\syspilot\scripts\powershell\init.ps1
#

$ErrorActionPreference = "Stop"

# Find syspilot root (3 levels up from this script)
$SyspilotRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$ProjectRoot = Get-Location

# Don't install into syspilot itself
if ($SyspilotRoot -eq $ProjectRoot) {
    Write-Host "Run this from your project directory, not from syspilot." -ForegroundColor Red
    exit 1
}

# Create .github/agents and copy Setup Agent
$AgentsDir = Join-Path $ProjectRoot ".github\agents"
New-Item -ItemType Directory -Path $AgentsDir -Force | Out-Null

$SetupAgentSource = Join-Path $SyspilotRoot ".github\agents\syspilot.setup.agent.md"
Copy-Item -Path $SetupAgentSource -Destination $AgentsDir -Force

Write-Host "Done. Open VS Code, start GitHub Copilot Chat, and select @syspilot.setup" -ForegroundColor Green
