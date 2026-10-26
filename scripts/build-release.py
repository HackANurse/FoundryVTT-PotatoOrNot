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
    for path in ROOT.rglob("*"):
        if not path.is_file() or dist in path.parents or ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        if relative == Path("module.json"):
            archive.writestr("module.json", (dist / "module.json").read_bytes())
        else:
            archive.write(path, relative)
print(dist)
