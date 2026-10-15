"""Repository checks run by CI and locally: python3 scripts/check_repo.py"""

import datetime
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "docs" / "implementation-plan.md"
PLAN_SECTIONS = ["Rezultat", "Platformă și stack existent", "Criteriu de acceptare"]
TECH_FIELDS = ["name", "package", "version", "repository", "authorized"]
# Exact versions only: 3.90.0, v1.2.3, 4.3-stable. Rejects ^, ~, >=, *, x, ranges.
EXACT_VERSION = re.compile(r"^v?\d+(\.\d+)*([-+][0-9A-Za-z.-]+)?$")
SKIP_DIRS = {".git", "references", "repos", "node_modules"}

errors = []


def error(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def split_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        error(path, "missing YAML frontmatter between '---' lines")
        return None, text
    try:
        return yaml.safe_load(match.group(1)) or {}, match.group(2)
    except yaml.YAMLError as exc:
        error(path, f"invalid YAML frontmatter: {exc}")
        return None, match.group(2)


def check_plan():
    if not PLAN.exists():
        error(PLAN, "file is missing")
        return
    meta, body = split_frontmatter(PLAN)
    if meta is None:
        return
    status = meta.get("status")
    if status not in ("draft", "approved"):
        error(PLAN, f"status must be 'draft' or 'approved', got {status!r}")
    technologies = meta.get("technologies")
    if not isinstance(technologies, list):
        error(PLAN, "technologies must be a list")
        return
    if status != "approved":
        return

    if not meta.get("approved_by"):
        error(PLAN, "approved_by is empty")
    try:
        datetime.date.fromisoformat(str(meta.get("approved_on")))
    except ValueError:
        error(PLAN, "approved_on must be a date in YYYY-MM-DD format")
    for section in PLAN_SECTIONS:
        # Placeholder text is kept in HTML comments, so a comment alone counts as empty.
        if not re.search(rf"^## {re.escape(section)}\n+[^#\s<]", body, re.M):
            error(PLAN, f"section '## {section}' is missing or empty")
    if not technologies:
        error(PLAN, "an approved plan needs at least one technology")
    for index, tech in enumerate(technologies):
        label = f"technologies[{index}]"
        if not isinstance(tech, dict):
            error(PLAN, f"{label} must be a mapping")
            continue
        label = f"{label} ({tech.get('name', '?')})"
        for field in TECH_FIELDS:
            if field not in tech or tech[field] in (None, ""):
                error(PLAN, f"{label} is missing '{field}'")
        if tech.get("authorized") is not True:
            error(PLAN, f"{label} is not authorized: true")
        if "version" in tech and not EXACT_VERSION.match(str(tech["version"])):
            error(PLAN, f"{label} version {tech['version']!r} is not an exact version")
        repository = str(tech.get("repository", ""))
        if repository and (not repository.startswith("https://") or "@" in repository.split("/")[2]):
            error(PLAN, f"{label} repository must be an https URL without credentials")


def check_skills():
    for skill in ROOT.glob(".claude/skills/*/SKILL.md"):
        meta, _ = split_frontmatter(skill)
        if meta is None:
            continue
        for field in ("name", "description"):
            if not meta.get(field):
                error(skill, f"frontmatter is missing '{field}'")


def markdown_files():
    for path in ROOT.rglob("*.md"):
        if not SKIP_DIRS.intersection(path.relative_to(ROOT).parts):
            yield path


def check_markdown():
    link = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        if re.search(r"^(<<<<<<<|>>>>>>>) ", text, re.M):
            error(path, "contains merge conflict markers")
        # Ignore links inside fenced code blocks.
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in link.findall(text):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            local = target.split("#")[0]
            if local and not (path.parent / local).exists():
                error(path, f"broken link to {target}")


check_plan()
check_skills()
check_markdown()

if errors:
    print("Checks failed:")
    for message in errors:
        print(f"  - {message}")
    sys.exit(1)
print("All checks passed.")
