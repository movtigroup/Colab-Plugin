#!/usr/bin/env python3
"""Repository validator for the colab ZCode plugin / اعتبارسنج مخزن پلاگین colab.

Checks / بررسی‌ها:
  1. marketplace.json parses and its single entry points at ./colab
  2. .zcode-plugin/plugin.json parses; name matches its directory; version is semver
  3. declared components (skills directory, .mcp.json) exist and stay inside the plugin root
  4. every SKILL.md has a well-formed `name`/`description` frontmatter

Usage / استفاده:  python scripts/validate.py
Exit code 0 = all checks passed / کد خروج ۰ یعنی همه‌ی بررسی‌ها موفق.
"""
import json
import re
import sys
from pathlib import Path

# Windows consoles (cp1256 etc.) cannot print Persian; force UTF-8 output.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
PLUGIN_ROOT = ROOT / "colab"
problems = []


def report(ok, ok_msg, fail_msg):
    print(("  OK   " if ok else "  FAIL ") + (ok_msg if ok else fail_msg))
    if not ok:
        problems.append(fail_msg)


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        report(False, "", f"{path.name}: {exc}")
        return None


print("== marketplace.json ==")
mp = read_json(ROOT / "marketplace.json")
if mp is not None:
    plugins = mp.get("plugins", [])
    report(len(plugins) == 1, "exactly one plugin entry", f"expected 1 entry, found {len(plugins)}")
    if plugins:
        entry = plugins[0]
        report(entry.get("name") == "colab", "entry name == colab", f"entry name is {entry.get('name')!r}")
        report(entry.get("source") == "./colab", "entry source == ./colab", f"source is {entry.get('source')!r}")

print("== colab/.zcode-plugin/plugin.json ==")
manifest = read_json(PLUGIN_ROOT / ".zcode-plugin" / "plugin.json")
if manifest is not None:
    report(manifest.get("name") == "colab", "name == colab (matches directory name)", f"name is {manifest.get('name')!r}")
    version = str(manifest.get("version", ""))
    report(bool(re.fullmatch(r"\d+\.\d+\.\d+", version)), f"version {version} is semver", "version is not semver")

    print("== declared components exist ==")
    skills = manifest.get("skills")
    if skills:
        skills_path = (PLUGIN_ROOT / str(skills)).resolve()
        inside = skills_path.is_relative_to(PLUGIN_ROOT.resolve())
        report(inside, "skills path stays inside plugin root", f"skills path escapes plugin root: {skills_path}")
        for skill in ("colab-mcp", "colab-cli"):
            report((skills_path / skill / "SKILL.md").exists(), f"skills/{skill}/SKILL.md exists", f"skills/{skill}/SKILL.md missing")

    mcp = manifest.get("mcpServers")
    if mcp:
        mcp_path = (PLUGIN_ROOT / str(mcp)).resolve()
        inside = mcp_path.is_relative_to(PLUGIN_ROOT.resolve())
        report(inside, "mcpServers path stays inside plugin root", f"mcpServers path escapes plugin root: {mcp_path}")
        report(mcp_path.is_file(), ".mcp.json exists", f".mcp.json missing at {mcp_path}")

    print("== skill frontmatter ==")
    skills_path = (PLUGIN_ROOT / str(manifest.get("skills", "skills"))).resolve()
    for skill in ("colab-mcp", "colab-cli"):
        sf = skills_path / skill / "SKILL.md"
        regexStr = r"^---\nname: (.+)\ndescription: (.+)\n---\n"
        if not sf.exists():
            continue
        text = sf.read_text(encoding="utf-8")
        m = re.match(regexStr, text)
        report(bool(m), f"{skill}/SKILL.md frontmatter well-formed", f"{skill}/SKILL.md frontmatter malformed")
        name = m.group(1).strip() if m else ""
        report(name == skill, f"{skill} frontmatter name matches directory", f"{skill} frontmatter name is {name!r}")

if problems:
    print(f"\nVALIDATION FAILED: {len(problems)} problem(s)")
    sys.exit(1)
print("\nALL CHECKS PASSED / همه‌ی بررسی‌ها موفق")
