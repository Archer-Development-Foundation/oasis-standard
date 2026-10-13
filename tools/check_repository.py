#!/usr/bin/env python3
"""Check documentation integrity and obvious publication hazards; no protocol tests."""

from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent


def repository_files():
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT, check=True, capture_output=True,
    )
    return sorted(set(result.stdout.decode().rstrip("\0").split("\0")) - {""})


def check():
    errors = []
    files = repository_files()
    required = {
        "README.md", "LICENSE", "NOTICE", "GOVERNANCE.md", "PATENTS.md",
        "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md",
        "asips/ASIP-0000-process.md", "conformance/scenarios.md",
    }
    for name in sorted(required - set(files)):
        errors.append(f"Missing required file: {name}")

    forbidden_names = {"AGENTS.md", "CLAUDE.md", ".env", ".DS_Store"}
    forbidden_dirs = {".agents", ".claude", ".codex", ".worktrees", "node_modules"}
    hazards = {
        "local user path": re.compile(r"/(?:Users|home)/[^\s/]+/"),
        "private planning link": re.compile(r"https?://(?:linear\.app|app\.notion\.com|chatgpt\.com/local)/"),
        "private infrastructure": re.compile(r"https?://[^\s/]+\.(?:supabase\.co|up\.railway\.app)"),
        "private key material": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "access token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk_(?:live|test)_[A-Za-z0-9]{12,})\b"),
        "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    }
    documents = {}
    for name in files:
        path = ROOT / name
        if path.is_symlink():
            errors.append(f"Symlink is not allowed in this publication: {name}")
            continue
        if any(part in forbidden_dirs for part in path.relative_to(ROOT).parts) or path.name in forbidden_names or path.name.startswith(".env."):
            errors.append(f"Private/context file: {name}")
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append(f"Unreadable or non-text publication file: {name}")
            continue
        for label, pattern in hazards.items():
            if pattern.search(text):
                errors.append(f"Possible {label}: {name} (inspect locally; value withheld)")
        if path.suffix == ".md":
            documents[name] = text
            # This package uses inline Markdown links; skip examples in fenced code.
            prose = re.sub(r"```.*?```", "", text, flags=re.S)
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose):
                target = target.strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme in {"https", "http"}:
                    continue
                if parsed.scheme or target.startswith("/"):
                    errors.append(f"Nonportable link in {name}: {target}")
                    continue
                resolved = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
                if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                    errors.append(f"Missing or out-of-repository link in {name}: {target}")
                elif str(resolved.relative_to(ROOT)) not in files:
                    errors.append(f"Link to unpublished file in {name}: {target}")

    specs = sorted(name for name in documents if re.match(r"specs/OASIS-\d{4}-", name))
    if len(specs) != 8:
        errors.append("Initial draft must contain all eight indexed specification documents")
    for name in specs:
        for field in ("Version", "Status", "Editors", "Updated", "Proposal"):
            if not re.search(rf"^\| {field} \|", documents[name], re.M):
                errors.append(f"Missing specification metadata {field}: {name}")

    if errors:
        print("Repository check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(files)} text files; local links, draft metadata, and publication-hazard checks.")
    print("This is a documentation check, not a full secret audit or protocol-conformance result.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
