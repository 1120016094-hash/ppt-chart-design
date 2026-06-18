#!/usr/bin/env python3
"""Provenance helpers for generated-image assets used in chart renders.

Upgrade-style chart workflows should lock the exact generated image that is approved for
compositing. The final render script should read from that locked asset path, not from an
mtime search result or an unrelated generated_images candidate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Dict, Iterable

from PIL import Image


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot(root: Path) -> Dict[str, Dict[str, object]]:
    files = {}
    if not root.exists():
        return files
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
            stat = path.stat()
            files[str(path)] = {"size": stat.st_size, "mtime": stat.st_mtime}
    return files


def image_size(path: Path):
    with Image.open(path) as im:
        return list(im.size)


def new_files(before: Dict[str, object], after: Dict[str, object]) -> Iterable[Path]:
    before_paths = set(before)
    for path in after:
        if path not in before_paths:
            yield Path(path)


def write_manifest(asset: Path, out: Path, prompt_summary: str = "", role: str = "approved_generated_asset") -> None:
    manifest = {
        "role": role,
        "approved_asset_path": str(asset),
        "sha256": sha256(asset),
        "size_bytes": asset.stat().st_size,
        "image_size": image_size(asset),
        "prompt_summary": prompt_summary,
    }
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def verify_manifest(manifest_path: Path) -> None:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    asset = Path(manifest["approved_asset_path"])
    if not asset.exists():
        raise FileNotFoundError(f"approved generated asset not found: {asset}")
    actual = sha256(asset)
    expected = manifest["sha256"]
    if actual != expected:
        raise ValueError(f"approved generated asset hash mismatch: {asset}")
    print(json.dumps({"ok": True, "asset": str(asset), "sha256": actual}, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    snap = sub.add_parser("snapshot")
    snap.add_argument("--root", required=True)
    snap.add_argument("--out", required=True)

    diff = sub.add_parser("diff")
    diff.add_argument("--before", required=True)
    diff.add_argument("--root", required=True)

    lock = sub.add_parser("lock")
    lock.add_argument("--asset", required=True)
    lock.add_argument("--out", required=True)
    lock.add_argument("--prompt-summary", default="")

    verify = sub.add_parser("verify")
    verify.add_argument("--manifest", required=True)

    args = parser.parse_args()
    if args.cmd == "snapshot":
        data = snapshot(Path(args.root))
        Path(args.out).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    elif args.cmd == "diff":
        before = json.loads(Path(args.before).read_text(encoding="utf-8"))
        after = snapshot(Path(args.root))
        print(json.dumps([str(p) for p in new_files(before, after)], ensure_ascii=False, indent=2))
    elif args.cmd == "lock":
        write_manifest(Path(args.asset), Path(args.out), args.prompt_summary)
    elif args.cmd == "verify":
        verify_manifest(Path(args.manifest))


if __name__ == "__main__":
    main()
