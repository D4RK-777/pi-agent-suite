#!/usr/bin/env python3
"""
Scan a project for obvious security issues.

Usage:
    python scan_project.py <path> [--format text|json]
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

DANGEROUS_PATTERNS = {
    ".py": [
        (r"\beval\s*\(", "eval() can execute arbitrary code"),
        (r"\bexec\s*\(", "exec() can execute arbitrary code"),
        (r"\bos\.system\s*\(", "os.system() is vulnerable to command injection"),
        (r"subprocess\.\w+\([^)]*shell\s*=\s*True", "subprocess shell=True is risky"),
        (r"\.execute\s*\(\s*f[\"']", "SQL f-strings are vulnerable to injection"),
    ],
    ".js": [
        (r"\beval\s*\(", "eval() can execute arbitrary code"),
        (r"\bnew\s+Function\s*\(", "Function constructor can execute arbitrary code"),
        (r"\.innerHTML\s*=", "innerHTML assignment is XSS-prone"),
        (r"child_process\.exec\s*\(", "child_process.exec() is command-injection prone"),
    ],
    ".ts": [
        (r"\beval\s*\(", "eval() can execute arbitrary code"),
        (r"dangerouslySetInnerHTML", "dangerouslySetInnerHTML is XSS-prone"),
        (r"\.innerHTML\s*=", "innerHTML assignment is XSS-prone"),
    ],
    ".go": [
        (r'exec\.Command\s*\(\s*"sh"', "shell execution can be command-injection prone"),
        (r'db\.Query\s*\([^)]*\+', "string concatenation in SQL query is vulnerable to injection"),
    ],
}

CONFIG_PATTERNS = [
    (r"DEBUG\s*[=:]\s*[Tt]rue", "Debug mode enabled"),
    (r"SSL_VERIFY\s*[=:]\s*[Ff]alse", "TLS verification disabled"),
    (r"verify\s*=\s*False", "TLS verification disabled"),
    (r"CORS_ALLOW_ALL_ORIGINS\s*=\s*True", "CORS allows all origins"),
    (r"NODE_TLS_REJECT_UNAUTHORIZED\s*[=:]\s*['\"]?0", "TLS verification disabled"),
]


def should_skip(path: Path, root: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.relative_to(root).parts)


def scan_file(filepath: Path) -> list[dict]:
    findings: list[dict] = []
    if filepath.suffix.lower() in SKIP_EXTENSIONS:
        return findings

    try:
        if filepath.stat().st_size > MAX_FILE_SIZE:
            return findings
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return findings

    patterns = DANGEROUS_PATTERNS.get(filepath.suffix.lower(), [])
    for line_number, line in enumerate(content.splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith("#") or stripped.startswith("//"):
            continue

        for pattern, rule in patterns:
            if re.search(pattern, line):
                findings.append(
                    {
                        "type": "code",
                        "severity": "high",
                        "file": str(filepath),
                        "line": line_number,
                        "rule": rule,
                        "snippet": line.strip()[:140],
                    }
                )

        for pattern, rule in CONFIG_PATTERNS:
            if re.search(pattern, line):
                findings.append(
                    {
                        "type": "config",
                        "severity": "medium",
                        "file": str(filepath),
                        "line": line_number,
                        "rule": rule,
                        "snippet": line.strip()[:140],
                    }
                )

    return findings


def check_project_hygiene(root: Path) -> list[dict]:
    findings: list[dict] = []
    gitignore = root / ".gitignore"
    if not gitignore.exists():
        findings.append(
            {
                "type": "hygiene",
                "severity": "medium",
                "file": str(root),
                "line": 0,
                "rule": "Missing .gitignore",
                "snippet": "",
            }
        )
        return findings

    content = gitignore.read_text(encoding="utf-8", errors="ignore")
    for pattern in [".env", "*.pem", "*.key"]:
        if pattern not in content:
            findings.append(
                {
                    "type": "hygiene",
                    "severity": "medium",
                    "file": str(gitignore),
                    "line": 0,
                    "rule": f".gitignore is missing '{pattern}'",
                    "snippet": "",
                }
            )

    return findings


def scan_project(root: Path) -> tuple[list[dict], int]:
    findings = check_project_hygiene(root)
    scanned = 0
    for file_path in root.rglob("*"):
        if not file_path.is_file() or should_skip(file_path, root):
            continue
        findings.extend(scan_file(file_path))
        scanned += 1
    return findings, scanned


def format_text(findings: list[dict], scanned: int) -> str:
    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    findings = sorted(findings, key=lambda item: severity_order.get(item["severity"], 9))

    lines = [f"Scanned {scanned} files", f"Found {len(findings)} issue(s)", ""]
    for finding in findings:
        location = f"{finding['file']}:{finding['line']}" if finding["line"] else finding["file"]
        lines.append(f"[{finding['severity'].upper()}] {finding['rule']}")
        lines.append(f"  Location: {location}")
        if finding["snippet"]:
            lines.append(f"  Code: {finding['snippet']}")
        lines.append("")
    return "\n".join(lines).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a first-pass security scan")
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
        print(format_text(findings, scanned))

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
