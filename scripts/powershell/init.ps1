# syspilot Bootstrap Script (Windows)
# 
# This script copies the Setup Agent to your project and configures VS Code.
# Run this once to bootstrap syspilot in your project.
#
# Usage: .\init.ps1
#

$ErrorActionPreference = "Stop"

# Find syspilot root (where this script lives)
$SyspilotRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$ProjectRoot = Get-Location

Write-Host "syspilot Bootstrap" -ForegroundColor Cyan
Write-Host "==================" -ForegroundColor Cyan
Write-Host ""
Write-Host "syspilot location: $SyspilotRoot"
Write-Host "Project location:  $ProjectRoot"
Write-Host ""

# Check if we're in the syspilot directory itself
if ($SyspilotRoot -eq $ProjectRoot) {
    Write-Host "[ERROR] Cannot install syspilot into itself!" -ForegroundColor Red
    Write-Host "        Please run this script from your project directory." -ForegroundColor Red
    Write-Host ""
    Write-Host "Example:" -ForegroundColor Yellow
    Write-Host "  cd C:\path\to\your\project" -ForegroundColor Yellow
    Write-Host "  C:\path\to\syspilot\scripts\powershell\init.ps1" -ForegroundColor Yellow
    exit 1
}

# Create .github/agents directory if it doesn't exist
$AgentsDir = Join-Path $ProjectRoot ".github\agents"
if (-not (Test-Path $AgentsDir)) {
    Write-Host "Creating .github/agents directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $AgentsDir -Force | Out-Null
}

# Copy the Setup Agent
$SetupAgentSource = Join-Path $SyspilotRoot "agents\syspilot.setup.agent.md"
$SetupAgentDest = Join-Path $AgentsDir "syspilot.setup.agent.md"

if (Test-Path $SetupAgentSource) {
    Write-Host "Copying Setup Agent..." -ForegroundColor Yellow
    Copy-Item -Path $SetupAgentSource -Destination $SetupAgentDest -Force
    Write-Host "  -> $SetupAgentDest" -ForegroundColor Green
} else {
    Write-Host "[WARN] Setup Agent not found at: $SetupAgentSource" -ForegroundColor Yellow
    Write-Host "       Creating minimal Setup Agent..." -ForegroundColor Yellow
    
    # Create minimal setup agent
    $MinimalAgent = @"
---
description: Install and update syspilot in this project.
---

# syspilot Setup Agent

I will help you install or update syspilot in this project.

Please provide the path to your syspilot installation directory.
"@
    Set-Content -Path $SetupAgentDest -Value $MinimalAgent
}

# Update or create .vscode/settings.json
$VscodeDir = Join-Path $ProjectRoot ".vscode"
$SettingsFile = Join-Path $VscodeDir "settings.json"

if (-not (Test-Path $VscodeDir)) {
    Write-Host "Creating .vscode directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $VscodeDir -Force | Out-Null
}

$SettingsToAdd = @{
    "chat.promptFilesRecommendations" = @{
        "syspilot.setup" = $true
    }
}

if (Test-Path $SettingsFile) {
    Write-Host "Updating VS Code settings..." -ForegroundColor Yellow
    try {
        $ExistingSettings = Get-Content $SettingsFile -Raw | ConvertFrom-Json -AsHashtable
        
        # Merge settings
        if (-not $ExistingSettings.ContainsKey("chat.promptFilesRecommendations")) {
            $ExistingSettings["chat.promptFilesRecommendations"] = @{}
        }
        $ExistingSettings["chat.promptFilesRecommendations"]["syspilot.setup"] = $true
        
        $ExistingSettings | ConvertTo-Json -Depth 10 | Set-Content $SettingsFile
    } catch {
        Write-Host "[WARN] Could not parse existing settings.json, creating new one" -ForegroundColor Yellow
        $SettingsToAdd | ConvertTo-Json -Depth 10 | Set-Content $SettingsFile
    }
} else {
    Write-Host "Creating VS Code settings..." -ForegroundColor Yellow
    $SettingsToAdd | ConvertTo-Json -Depth 10 | Set-Content $SettingsFile
}

Write-Host ""
Write-Host "[OK] Bootstrap complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Open this project in VS Code"
Write-Host "2. Open Copilot Chat (Ctrl+Shift+I)"
Write-Host "3. Type: @syspilot.setup"
Write-Host "4. Follow the Setup Agent's instructions"
Write-Host ""
