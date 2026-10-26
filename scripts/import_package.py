#!/usr/bin/env python3
"""Import the verified EARG ZIP into a cloned repository (does not commit/push)."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
import zipfile

PREFIX = "EARG_12GB_Codex_Research_Package/"
REPLACE_BOOTSTRAP = {".gitignore", "AGENTS.md", "CODEX_START_PROMPT.md", "PROPOSAL_12GB.md", "README.md"}

def import_archive(zip_path: Path, repo: Path) -> None:
    if not (repo / ".git").exists():
        raise ValueError("Run from the EARG Git repository root.")
    with zipfile.ZipFile(zip_path) as archive:
        filenames = [x for x in archive.namelist() if not x.endswith("/")]
        if not all(x.startswith(PREFIX) for x in filenames):
            raise ValueError("This is not the expected EARG package.")
        files = {x[len(PREFIX):]: archive.read(x) for x in filenames}
        manifest = json.loads(files["PACKAGE_MANIFEST.json"].decode("utf-8"))
        items = manifest["files"]
        if len(items) != 48 or {e["path"] for e in items} != set(files) - {"PACKAGE_MANIFEST.json"}:
            raise ValueError("Incomplete archive or manifest mismatch.")
        for item in items:
            data = files[item["path"]]
            if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
                raise ValueError("File integrity check failed: " + item["path"])
        targets = []
        for relative, content in files.items():
            p = PurePosixPath(relative)
            if p.is_absolute() or ".." in p.parts or not p.parts:
                raise ValueError("Unsafe path in package: " + relative)
            target = repo.joinpath(*p.parts)
            if target.is_symlink():
                raise ValueError("Refusing to overwrite symlink: " + relative)
            if target.exists() and target.read_bytes() != content and relative not in REPLACE_BOOTSTRAP:
                raise ValueError("Refusing to overwrite existing file: " + relative)
            targets.append((target, content))
        for target, content in targets:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
    print(f"Verified {len(items)} files; imported {len(targets)} files.")
    print("Run: python scripts/verify_package.py")
    print("Then: pip install -e '.[dev]' && pytest -q")
    print("Review and push: git status; git diff --stat; git add -A; git commit; git push")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python scripts/import_package.py PATH_TO_EARG_ZIP")
    import_archive(Path(sys.argv[1]).expanduser().resolve(), Path.cwd())
