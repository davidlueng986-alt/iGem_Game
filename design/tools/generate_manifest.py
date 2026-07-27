#!/usr/bin/env python3
"""Generate deterministic SHA-256 manifests for the production pack."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

EXCLUDED = {"MANIFEST.md", "manifest.sha256"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def kind(path: Path) -> str:
    mapping = {
        ".md": "Markdown",
        ".pdf": "PDF",
        ".py": "Python",
        ".json": "JSON",
        ".sha256": "Checksum",
    }
    return mapping.get(path.suffix.lower(), path.suffix.lstrip(".").upper() or "File")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()

    root = Path(args.root).resolve()
    files = sorted(
        p
        for p in root.rglob("*")
        if p.is_file() and p.relative_to(root).as_posix() not in EXCLUDED
    )

    records: list[tuple[str, int, str, str]] = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        records.append((rel, path.stat().st_size, kind(path), sha256(path)))

    checksum_text = "".join(f"{digest}  {rel}\n" for rel, _, _, digest in records)
    (root / "manifest.sha256").write_text(checksum_text, encoding="utf-8", newline="\n")

    total = sum(size for _, size, _, _ in records)
    rows = "\n".join(
        f"| `{rel}` | {file_kind} | {size} | `{digest}` |"
        for rel, size, file_kind, digest in records
    )
    manifest = f"""# 《微界工程師：生命迴路》檔案 Manifest

> 產生日期：2026-07-27｜演算法：SHA-256｜收錄檔案：{len(records)}｜收錄總大小：{total} bytes

本表由 `tools/generate_manifest.py` 產生。為避免 checksum 自我遞迴，`MANIFEST.md` 與 `manifest.sha256` 本身不在清單內；其餘根目錄下的所有檔案均應被列出。

驗證命令：

```bash
sha256sum -c manifest.sha256
```

| Relative path | Type | Bytes | SHA-256 |
|---|---|---:|---|
{rows}
"""
    (root / "MANIFEST.md").write_text(manifest, encoding="utf-8", newline="\n")
    print(f"Generated {len(records)} records; {total} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
