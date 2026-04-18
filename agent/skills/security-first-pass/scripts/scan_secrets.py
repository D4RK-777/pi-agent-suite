#!/usr/bin/env python3
"""
Scan a project for obvious hardcoded secrets.

Usage:
    python scan_secrets.py <path> [--format text|json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKIP_DIRS = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    "dist",
    "build",
    ".next",
    ".turbo",
    ".pytest_cache",
}

SKIP_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".ico",
    ".pdf",
    ".zip",
    ".gz",
    ".tar",
    ".exe",
    ".dll",
    ".pyc",
}

MAX_FILE_SIZE = 1_000_000

SECRET_PATTERNS = [
    ("AWS Access Key ID", r"AKIA[0-9A-Z]{16}"),
    ("GitHub Token", r"gh[ps]_[A-Za-z0-9_]{36,}"),
    ("GitLab Token", r"glpat-[A-Za-z0-9\-]{20,}"),
    ("Slack Token", r"xox[baprs]-[A-Za-z0-9\-]{10,}"),
    ("Stripe Secret Key", r"sk_live_[A-Za-z0-9]{24,}"),
    ("SendGrid API Key", r"SG\.[A-Za-z0-9\-_]{22}\.[A-Za-z0-9\-_]{43}"),
    ("Google API Key", r"AIza[0-9A-Za-z\-_]{35}"),
    ("Private Key", r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ("Database URL with password", r"(?i)(mysql|postgres|postgresql|mongodb|redis)://[^:\s]+:[^@\s]+@"),
    ("Hardcoded password", r'(?i)(password|passwd|pwd)\s*[=:]\s*["\'][^"\']{8,}["\']'),
    ("Hardcoded API key", r'(?i)(api_key|apikey|secret_key)\s*[=:]\s*["\'][^"\']{8,}["\']'),
]

FALSE_POSITIVE_HINTS = {
    "example",
    "changeme",
    "placeholder",
    "dummy",
    "sample",
    "todo",
    "fixme",
    "process.env",
    "os.environ",
    "getenv",
    "${",
}


def should_skip(path: Path, root: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.relative_to(root).parts)


def likely_false_positive(line: str) -> bool:
    lowered = line.lower()
    return any(marker in lowered for marker in FALSE_POSITIVE_HINTS)


def scan_project(root: Path) -> tuple[list[dict], int]:
    findings: list[dict] = []
    scanned = 0
    for file_path in root.rglob("*"):
        if not file_path.is_file() or should_skip(file_path, root):
            continue
        if file_path.suffix.lower() in SKIP_EXTENSIONS:
            continue
        try:
            if file_path.stat().st_size > MAX_FILE_SIZE:
                continue
            content = file_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        for line_number, line in enumerate(content.splitlines(), 1):
            if likely_false_positive(line):
                continue
            for label, pattern in SECRET_PATTERNS:
                if re.search(pattern, line):
                    findings.append(
                        {
                            "type": label,
                            "file": str(file_path),
                            "line": line_number,
                            "snippet": line.strip()[:140],
                        }
                    )
        scanned += 1

    return findings, scanned


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan for obvious hardcoded secrets")
    parser.add_argument("path", help="Project directory to scan")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        return 1

    findings, scanned = scan_project(root)

    if args.format == "json":
        print(json.dumps({"scanned_files": scanned, "total_findings": len(findings), "findings": findings}, indent=2))
    else:
        print(f"Scanned {scanned} files")
        print(f"Found {len(findings)} potential secret(s)")
        print()
        for finding in findings:
            print(f"[{finding['type']}] {finding['file']}:{finding['line']}")
            print(f"  {finding['snippet']}")
            print()

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
