# syspilot Bootstrap Script (Windows)
#
# Downloads the Setup Agent to your project via curl. That's it.
# The Setup Agent handles everything else interactively.
#
# Usage: irm https://raw.githubusercontent.com/enthali/syspilot/main/scripts/powershell/init.ps1 | iex
#    or: C:\path\to\syspilot\scripts\powershell\init.ps1
#

$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Path ".github\agents" -Force | Out-Null

$Url = "https://raw.githubusercontent.com/enthali/syspilot/main/.github/agents/syspilot.setup.agent.md"
$Destination = Join-Path (Get-Location) ".github\agents\syspilot.setup.agent.md"
Invoke-WebRequest -Uri $Url -OutFile $Destination -UseBasicParsing

Write-Host "Done. Open VS Code, start GitHub Copilot Chat, and select @syspilot.setup" -ForegroundColor Green
