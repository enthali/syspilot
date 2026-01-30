# Build Sphinx documentation
# Usage: .\build.ps1 [clean]

param(
    [switch]$Clean
)

$ErrorActionPreference = "Stop"
$DocsDir = $PSScriptRoot
$BuildDir = Join-Path $DocsDir "_build"

if ($Clean) {
    Write-Host "Cleaning build directory..." -ForegroundColor Yellow
    if (Test-Path $BuildDir) {
        Remove-Item -Recurse -Force $BuildDir
    }
}

Write-Host "Building HTML documentation..." -ForegroundColor Cyan

# Use uv run if available, otherwise direct call
if (Get-Command uv -ErrorAction SilentlyContinue) {
    uv run sphinx-build -b html $DocsDir (Join-Path $BuildDir "html") --keep-going
} else {
    sphinx-build -b html $DocsDir (Join-Path $BuildDir "html") --keep-going
}

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[OK] Documentation built successfully!" -ForegroundColor Green
    Write-Host "     Open: $BuildDir\html\index.html" -ForegroundColor Gray
} else {
    Write-Host "`n[FAIL] Documentation build failed!" -ForegroundColor Red
    exit $LASTEXITCODE
}
