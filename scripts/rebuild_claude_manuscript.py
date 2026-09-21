#!/usr/bin/env python3
"""Rebuild archived prose from literal text operations; never execute source commands."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
folder = root / "sources/gui-xiang-yi-qi"
operations = json.loads((folder / "文学写入记录.json").read_text())["operations"]
virtual = {}
for op in operations:
    path = op["path"]
    if op["kind"] == "write":
        virtual[path] = op["text"]
    elif op["kind"] == "append":
        virtual[path] += op["text"]
    elif op["kind"] == "replace":
        assert virtual[path].count(op["old"]) == op["expected_matches"], op["line"]
        virtual[path] = virtual[path].replace(op["old"], op["new"], op["count"])
    elif op["kind"] == "replace_tail":
        assert virtual[path].count(op["start"]) == 1, op["line"]
        virtual[path] = virtual[path][:virtual[path].find(op["start"])] + op["text"]
    else:
        raise ValueError(op["kind"])
prose = virtual["/home/claude/归乡疫期.md"].encode()
expected = (folder / "Claude合作稿-重建.md").read_bytes()
assert prose == expected, "Rebuilt prose differs"
print("Verified manuscript reconstruction:", hashlib.sha256(prose).hexdigest())
