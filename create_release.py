#!/usr/bin/env python3
"""
ThinkPage Release Packager
Generates a clean source code ZIP release archive.

Usage:
    python3 create_release.py [--output ThinkPage-release.zip]
"""

import argparse
import datetime
import os
import sys
import zipfile

# Files and directories to explicitly include in the release
INCLUDE_FILES = [
    "index.html",
    "sw.js",
    "manifest.webmanifest",
    "app-icon.svg",
    "server.py",
    "create_release.py",
    "README.md",
    "LICENSE",
]

# Patterns or directory names to exclude
EXCLUDE_PATTERNS = [
    ".git",
    ".github",
    ".DS_Store",
    "__pycache__",
    ".pytest_cache",
    ".vscode",
    ".idea",
]

def create_release_zip(output_path=None):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)

    if not output_path:
        timestamp = datetime.datetime.now().strftime("%Y%m%d")
        output_path = f"ThinkPage-release-{timestamp}.zip"

    output_abs_path = os.path.abspath(output_path)
    output_filename = os.path.basename(output_abs_path)

    print("=" * 60)
    print("  📦 Creating ThinkPage Release ZIP Archive")
    print("=" * 60)

    zipped_files = []

    with zipfile.ZipFile(output_abs_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(root_dir):
            # Prune excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_PATTERNS and not d.startswith('.')]

            for file in files:
                if file in EXCLUDE_PATTERNS or file == output_filename or file.endswith('.zip') or file.startswith('.'):
                    continue

                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, root_dir)

                top_folder = rel_path.split(os.sep)[0]
                if top_folder in EXCLUDE_PATTERNS or top_folder.startswith('.'):
                    continue

                zipf.write(full_path, rel_path)
                file_size = os.path.getsize(full_path)
                zipped_files.append((rel_path, file_size))
                print(f"  + Added: {rel_path} ({file_size:,} bytes)")

    total_size = os.path.getsize(output_abs_path)

    print("=" * 60)
    print(f"  ✅ Release ZIP created successfully!")
    print(f"  • File: {output_abs_path}")
    print(f"  • Size: {total_size / 1024:.2f} KB ({total_size:,} bytes)")
    print(f"  • Total files archived: {len(zipped_files)}")
    print("=" * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a ThinkPage Source ZIP Release")
    parser.add_argument("-o", "--output", type=str, help="Output ZIP file path (default: ThinkPage-release-YYYYMMDD.zip)")
    args = parser.parse_args()

    create_release_zip(args.output)
