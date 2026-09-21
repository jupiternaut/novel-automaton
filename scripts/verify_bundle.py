#!/usr/bin/env python3
"""Read-only check of archive inventory and source snapshots."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "MANIFEST.json").read_text())
expected = {x["path"] for x in manifest["files"]}
actual = {
    p.relative_to(root).as_posix()
    for p in root.rglob("*")
    if p.is_file() and ".git" not in p.relative_to(root).parts
    and "__pycache__" not in p.relative_to(root).parts
    and p.name not in {"MANIFEST.json", ".DS_Store"}
}
assert actual == expected, {"missing": sorted(expected-actual), "extra": sorted(actual-expected)}
for entry in manifest["files"]:
    data = (root / entry["path"]).read_bytes()
    assert len(data) == entry["bytes"], entry["path"]
    assert hashlib.sha256(data).hexdigest() == entry["sha256"], entry["path"]
for source in json.loads((root / "references/source-snapshots.json").read_text()):
    if source.get("missing"):
        continue
    data = (root / "references/snapshots" / source["path"]).read_bytes()
    assert hashlib.sha256(data).hexdigest() == source["sha256"], source["path"]
subprocess.run([sys.executable, str(root/"scripts/rebuild_claude_manuscript.py")], check=True)
print("Verified", len(expected), "payload files; MANIFEST.json excludes itself by design.")
