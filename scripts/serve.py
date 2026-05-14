#!/usr/bin/env python3
"""Watch content/ → auto-rebuild → auto-refresh browser."""

import subprocess
import sys
from pathlib import Path

from livereload import Server

ROOT = Path(__file__).parent.parent

def rebuild():
    print("Rebuilding...", flush=True)
    subprocess.run([sys.executable, str(ROOT / "build.py")], check=True)

def main():
    rebuild()

    server = Server()
    server.watch(str(ROOT / "content"), rebuild)
    server.watch(str(ROOT / "docs" / "style.css"))
    server.watch(str(ROOT / "docs" / "app.js"))

    print("Serving at http://localhost:5500  (auto-rebuild + auto-refresh)")
    server.serve(root=str(ROOT / "docs"), port=5500, open_url_delay=1)

if __name__ == "__main__":
    main()
