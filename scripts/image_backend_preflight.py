#!/usr/bin/env python3
"""Check whether the built-in image tool produced local files for chart workflows.

The built-in image tool may show a visible preview without creating an accessible file in
`$CODEX_HOME/generated_images`. Upgrade chart styles need a concrete local image file for
compositing. This skill intentionally does not call or recommend external generators such
as Dreamina; it only reports whether the built-in image output directory is observable.
"""
from __future__ import annotations

import json
import os
from pathlib import Path


def latest_image_mtime(root: Path) -> float | None:
    if not root.exists():
        return None
    latest = None
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
            mtime = path.stat().st_mtime
            latest = mtime if latest is None else max(latest, mtime)
    return latest


def main() -> None:
    home = Path.home()
    codex_home = Path(os.environ.get("CODEX_HOME", home / ".codex"))
    generated_root = codex_home / "generated_images"
    downloads_dir = home / "Downloads"
    manual_save_dir = home / "outputs/ppt-chart-design-assets"
    manual_save_dir.mkdir(parents=True, exist_ok=True)

    report: dict[str, object] = {
        "codex_home": str(codex_home),
        "generated_images_root": str(generated_root),
        "default_download_dir": str(downloads_dir),
        "manual_save_dir": str(manual_save_dir),
        "download_quick_open_terminal": f"open {downloads_dir}",
        "download_quick_open_finder": f"Finder -> Downloads, or Finder -> Go -> Go to Folder... -> {downloads_dir}",
        "manual_save_quick_open_terminal": f"open {manual_save_dir}",
        "manual_save_quick_open_finder": f"Finder -> Go -> Go to Folder... -> {manual_save_dir}",
        "generated_images_root_exists": generated_root.exists(),
        "generated_images_root_writable": os.access(generated_root, os.W_OK) if generated_root.exists() else False,
        "manual_save_dir_exists": manual_save_dir.exists(),
        "manual_save_dir_writable": os.access(manual_save_dir, os.W_OK) if manual_save_dir.exists() else False,
        "latest_generated_image_mtime": latest_image_mtime(generated_root),
        "allowed_backend": "built_in_image_gen_only",
        "external_backends_allowed": False,
        "blocking_reason": None,
    }

    if not generated_root.exists():
        report["blocking_reason"] = "Built-in image output directory does not exist."
    elif not report["generated_images_root_writable"]:
        report["blocking_reason"] = (
            "Built-in image output directory is not writable from the current tool sandbox. "
            "Use before/after snapshot after image generation; if no new file appears, stop "
            f"and ask the user to download the preview image, check {downloads_dir}, then "
            f"move or save it under {manual_save_dir}. Tell the user they can quickly open "
            f"Downloads with `open {downloads_dir}` and the target folder with "
            f"`open {manual_save_dir}`. "
            "Do not call external generators."
        )

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
