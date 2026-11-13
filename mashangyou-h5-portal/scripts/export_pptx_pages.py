#!/usr/bin/env python3
"""Export PowerPoint slides to sequential JPG files for mashangyou-style H5 stacks.

Requires: Windows + Microsoft PowerPoint + pywin32
  pip install pywin32
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def export(pptx: Path, out_dir: Path, width: int = 1200) -> int:
    try:
        import win32com.client  # type: ignore
    except ImportError:
        print("Missing pywin32. Run: pip install pywin32", file=sys.stderr)
        sys.exit(1)

    if not pptx.is_file():
        print(f"PPTX not found: {pptx}", file=sys.stderr)
        sys.exit(1)

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    app = win32com.client.Dispatch("PowerPoint.Application")
    app.Visible = 1
    try:
        pres = app.Presentations.Open(str(pptx.resolve()), WithWindow=False)
        sw = float(pres.PageSetup.SlideWidth)
        sh = float(pres.PageSetup.SlideHeight)
        height = max(1, int(width * sh / sw))
        count = int(pres.Slides.Count)
        print(f"slides={count} size={width}x{height}")
        for i in range(1, count + 1):
            dest = out_dir / f"{i:02d}.jpg"
            pres.Slides(i).Export(str(dest.resolve()), "JPG", width, height)
            print(f"  {dest.name}  {dest.stat().st_size} bytes")
        pres.Close()
        return count
    finally:
        app.Quit()


def main() -> None:
    parser = argparse.ArgumentParser(description="Export PPTX slides to JPG sequence")
    parser.add_argument("--pptx", required=True, help="Path to .pptx")
    parser.add_argument("--out", required=True, help="Output directory for 01.jpg…")
    parser.add_argument("--width", type=int, default=1200, help="Export width in px")
    args = parser.parse_args()
    n = export(Path(args.pptx), Path(args.out), args.width)
    print(f"DONE count={n}")


if __name__ == "__main__":
    main()
