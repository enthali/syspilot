#!/usr/bin/env python3
"""Build Sphinx documentation. Usage: uv run python docs-build.py [clean]"""
import subprocess
import shutil
import sys
from pathlib import Path


def main():
    docs_dir = Path(__file__).parent.resolve()
    build_dir = docs_dir / "_build"

    if len(sys.argv) > 1 and sys.argv[1] == "clean":
        print("Cleaning build directory...")
        if build_dir.exists():
            shutil.rmtree(build_dir)

    print("Building HTML documentation...")
    result = subprocess.run(
        ["uv", "run", "sphinx-build", "-b", "html",
         str(docs_dir), str(build_dir / "html"), "-W", "--keep-going"]
    )

    if result.returncode == 0:
        print(f"\n[OK] Documentation built successfully!")
        print(f"     Open: {build_dir / 'html' / 'index.html'}")
    else:
        print(f"\n[FAIL] Documentation build failed!")
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
