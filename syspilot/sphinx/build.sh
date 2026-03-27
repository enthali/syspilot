#!/bin/bash
# Build Sphinx documentation
# Usage: ./build.sh [clean]

set -e

DOCS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="$DOCS_DIR/_build"

if [ "$1" = "clean" ]; then
    echo "Cleaning build directory..."
    rm -rf "$BUILD_DIR"
fi

echo "Building HTML documentation..."

# Use uv run if available, otherwise direct call
if command -v uv &> /dev/null; then
    uv run sphinx-build -b html "$DOCS_DIR" "$BUILD_DIR/html" -W --keep-going
else
    sphinx-build -b html "$DOCS_DIR" "$BUILD_DIR/html" -W --keep-going
fi

if [ $? -eq 0 ]; then
    echo ""
    echo "[OK] Documentation built successfully!"
    echo "     Open: $BUILD_DIR/html/index.html"
else
    echo ""
    echo "[FAIL] Documentation build failed!"
    exit 1
fi
