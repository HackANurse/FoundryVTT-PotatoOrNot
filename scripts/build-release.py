#!/usr/bin/env python3
"""Build a GitHub release ZIP and manifest for this GPL-3.0 module."""
from pathlib import Path
import json
import os
import re
import zipfile

ROOT = Path(__file__).resolve().parent.parent
repo = os.environ.get("POTATO_OR_NOT_REPO", "")
if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
    raise SystemExit("Set POTATO_OR_NOT_REPO to your GitHub owner/repo")
manifest = json.loads((ROOT / "module.json").read_text())
version = manifest["version"]
base = f"https://github.com/{repo}"
manifest.update(url=base, manifest=f"{base}/releases/latest/download/module.json",
                download=f"{base}/releases/download/v{version}/module.zip",
                bugs=f"{base}/issues")
dist = ROOT / "dist"
dist.mkdir(exist_ok=True)
(dist / "module.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
with zipfile.ZipFile(dist / "module.zip", "w", zipfile.ZIP_DEFLATED) as archive:
    files = [Path("module.json"), Path("LICENSE"), Path("README.md"),
             Path("scripts/main.js"), Path("scripts/constants.js"),
             Path("scripts/lib.js"), Path("styles/styles.css"),
             Path("templates/potato-template.hbs")]
    files.extend(Path("languages") / path.name for path in sorted((ROOT / "languages").glob("*.json")))
    for relative in files:
        path = ROOT / relative
        if not path.is_file():
            raise SystemExit(f"Missing release file: {relative}")
        if relative == Path("module.json"):
            archive.writestr("module.json", (dist / "module.json").read_bytes())
        else:
            archive.write(path, relative)
print(dist)
