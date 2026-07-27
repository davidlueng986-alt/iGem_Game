#!/usr/bin/env python3
"""Validate the iGEM 2026 game production documentation pack.

Checks are intentionally deterministic and local: required files, Markdown links,
fenced code blocks, Markdown table widths, unique decision/claim definitions,
key cross-document baselines, source PDF integrity, and basic document sizes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

try:
    from pypdf import PdfReader
except Exception:  # pragma: no cover - optional for downstream users
    PdfReader = None  # type: ignore[assignment]


REQUIRED_FILES = [
    "README_START_HERE.md",
    "18_INDEPENDENT_PRODUCTION_READINESS_AUDIT.md",
    "02_GAME_DESIGN_DOCUMENT.md",
    "03_TECHNICAL_DESIGN_DOCUMENT.md",
    "04_ASSET_LIST_AND_PRODUCTION_GUIDELINES.md",
    "05_PROJECT_MANAGEMENT_PLAN.md",
    "06_QA_TEST_PLAN.md",
    "19_AI_ASSISTED_DEVELOPMENT_PLAYBOOK.md",
    "20_OPEN_DECISIONS_REGISTER.md",
    "21_AI_TASK_PACKET_TEMPLATE.md",
    "22_SOURCE_AND_CLAIM_REGISTER.md",
    "AGENTS.md",
    "23_DELIVERY_VALIDATION_REPORT.md",
    "24_LOGIC_CAMERA_AND_CHAPTER_2_8_AUDIT.md",
    "MANIFEST.md",
    "manifest.sha256",
    "tools/generate_manifest.py",
    "tools/validate_v2_logic.py",
    "sources/TEAM-PDF-2026-INTRO.pdf",
]

GENERATED_DOCS = [
    "README_START_HERE.md",
    "18_INDEPENDENT_PRODUCTION_READINESS_AUDIT.md",
    "02_GAME_DESIGN_DOCUMENT.md",
    "03_TECHNICAL_DESIGN_DOCUMENT.md",
    "04_ASSET_LIST_AND_PRODUCTION_GUIDELINES.md",
    "05_PROJECT_MANAGEMENT_PLAN.md",
    "06_QA_TEST_PLAN.md",
    "19_AI_ASSISTED_DEVELOPMENT_PLAYBOOK.md",
    "20_OPEN_DECISIONS_REGISTER.md",
    "21_AI_TASK_PACKET_TEMPLATE.md",
    "22_SOURCE_AND_CLAIM_REGISTER.md",
    "AGENTS.md",
    "23_DELIVERY_VALIDATION_REPORT.md",
    "24_LOGIC_CAMERA_AND_CHAPTER_2_8_AUDIT.md",
    "MANIFEST.md",
]


@dataclass
class Finding:
    severity: str
    check: str
    file: str
    line: int | None
    detail: str


@dataclass
class Result:
    root: str
    markdown_files: int
    checked_links: int
    tables: int
    qa_cases: int
    decision_definitions: int
    claim_definitions: int
    source_pdf_pages: int | None
    source_pdf_sha256: str | None
    manifest_files: int | None
    manifest_bytes: int | None
    errors: int
    warnings: int
    findings: list[Finding]


def iter_markdown(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def is_fence(line: str) -> tuple[str, int] | None:
    match = re.match(r"^\s*(`{3,}|~{3,})", line)
    if not match:
        return None
    token = match.group(1)
    return token[0], len(token)


def split_table_row(line: str) -> list[str]:
    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|") and not text.endswith(r"\|"):
        text = text[:-1]

    cells: list[str] = []
    current: list[str] = []
    in_code = False
    escaped = False
    i = 0
    while i < len(text):
        ch = text[i]
        if escaped:
            current.append(ch)
            escaped = False
        elif ch == "\\":
            current.append(ch)
            escaped = True
        elif ch == "`":
            in_code = not in_code
            current.append(ch)
        elif ch == "|" and not in_code:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
        i += 1
    cells.append("".join(current).strip())
    return cells


def is_separator_row(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells)


def find_links(text: str) -> Iterable[tuple[int, str]]:
    in_fence = False
    fence_char = ""
    fence_len = 0
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for lineno, line in enumerate(text.splitlines(), 1):
        fence = is_fence(line)
        if fence:
            ch, length = fence
            if not in_fence:
                in_fence, fence_char, fence_len = True, ch, length
            elif ch == fence_char and length >= fence_len:
                in_fence = False
            continue
        if in_fence:
            continue
        for match in pattern.finditer(line):
            raw = match.group(1).strip()
            if raw.startswith("<") and ">" in raw:
                raw = raw[1 : raw.index(">")]
            else:
                # Drop an optional Markdown title after whitespace.
                raw = re.split(r"\s+[\"']", raw, maxsplit=1)[0]
            yield lineno, raw


def add(findings: list[Finding], severity: str, check: str, file: Path | str, line: int | None, detail: str) -> None:
    findings.append(Finding(severity, check, str(file), line, detail))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    findings: list[Finding] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            add(findings, "ERROR", "required-file", rel, None, "Required file is missing")

    markdown = iter_markdown(root)
    checked_links = 0
    table_count = 0

    for path in markdown:
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        # Fenced code blocks.
        in_fence = False
        fence_char = ""
        fence_len = 0
        fence_start = 0
        for lineno, line in enumerate(lines, 1):
            fence = is_fence(line)
            if not fence:
                continue
            ch, length = fence
            if not in_fence:
                in_fence, fence_char, fence_len, fence_start = True, ch, length, lineno
            elif ch == fence_char and length >= fence_len:
                in_fence = False
        if in_fence:
            add(findings, "ERROR", "code-fence", rel, fence_start, "Unclosed fenced code block")

        # Relative links.
        for lineno, target in find_links(text):
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:", "sandbox:")):
                continue
            checked_links += 1
            target_path = unquote(target.split("#", 1)[0])
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                add(findings, "WARNING", "relative-link", rel, lineno, f"Link leaves pack root: {target}")
                continue
            if not resolved.exists():
                add(findings, "ERROR", "relative-link", rel, lineno, f"Broken relative link: {target}")

        # Markdown tables: detect header + separator and verify body widths.
        in_code = False
        fchar = ""
        flen = 0
        i = 0
        while i + 1 < len(lines):
            fence = is_fence(lines[i])
            if fence:
                ch, length = fence
                if not in_code:
                    in_code, fchar, flen = True, ch, length
                elif ch == fchar and length >= flen:
                    in_code = False
                i += 1
                continue
            if in_code:
                i += 1
                continue
            if "|" in lines[i] and is_separator_row(lines[i + 1]):
                header_cells = len(split_table_row(lines[i]))
                separator_cells = len(split_table_row(lines[i + 1]))
                table_count += 1
                if header_cells != separator_cells:
                    add(findings, "ERROR", "table-width", rel, i + 2, f"Header has {header_cells} cells; separator has {separator_cells}")
                j = i + 2
                while j < len(lines) and lines[j].strip().startswith("|"):
                    row_cells = len(split_table_row(lines[j]))
                    if row_cells != header_cells:
                        add(findings, "ERROR", "table-width", rel, j + 1, f"Expected {header_cells} cells; found {row_cells}")
                    j += 1
                i = j
                continue
            i += 1

    # Generated docs should not be empty shells.
    for rel in GENERATED_DOCS:
        path = root / rel
        if path.is_file() and path.stat().st_size < 2_000:
            add(findings, "ERROR", "document-size", rel, None, f"Generated document is unexpectedly small: {path.stat().st_size} bytes")

    agents = root / "AGENTS.md"
    if agents.is_file() and agents.stat().st_size > 32 * 1024:
        add(findings, "WARNING", "agents-size", "AGENTS.md", None, "AGENTS.md exceeds 32 KiB; some agents may truncate instructions")

    # Unique definition IDs in their authoritative registers.
    decision_text = (root / "20_OPEN_DECISIONS_REGISTER.md").read_text(encoding="utf-8") if (root / "20_OPEN_DECISIONS_REGISTER.md").is_file() else ""
    decision_ids = re.findall(r"^\|\s*`?(DEC-[A-Z0-9-]+)`?\s*\|", decision_text, flags=re.MULTILINE)
    for duplicate in sorted({x for x in decision_ids if decision_ids.count(x) > 1}):
        add(findings, "ERROR", "duplicate-decision-id", "20_OPEN_DECISIONS_REGISTER.md", None, duplicate)

    claim_text = (root / "22_SOURCE_AND_CLAIM_REGISTER.md").read_text(encoding="utf-8") if (root / "22_SOURCE_AND_CLAIM_REGISTER.md").is_file() else ""
    claim_ids = re.findall(r"^\| `(HG-[A-Z0-9-]+|SIM-[A-Z0-9-]+|APT-[A-Z0-9-]+|SAFE-[A-Z0-9-]+|ROLE-[A-Z0-9-]+|COMM-[A-Z0-9-]+)` \|", claim_text, flags=re.MULTILINE)
    for duplicate in sorted({x for x in claim_ids if claim_ids.count(x) > 1}):
        add(findings, "ERROR", "duplicate-claim-id", "22_SOURCE_AND_CLAIM_REGISTER.md", None, duplicate)

    qa_text = (root / "06_QA_TEST_PLAN.md").read_text(encoding="utf-8") if (root / "06_QA_TEST_PLAN.md").is_file() else ""
    qa_ids = re.findall(r"^\| (QA-[A-Z0-9-]+) \|", qa_text, flags=re.MULTILINE)
    if len(qa_ids) < 80:
        add(findings, "WARNING", "qa-coverage", "06_QA_TEST_PLAN.md", None, f"Only {len(qa_ids)} QA cases detected")
    for duplicate in sorted({x for x in qa_ids if qa_ids.count(x) > 1}):
        add(findings, "ERROR", "duplicate-qa-id", "06_QA_TEST_PLAN.md", None, duplicate)

    # Cross-document baseline checks.
    baseline_docs = [
        "README_START_HERE.md",
        "02_GAME_DESIGN_DOCUMENT.md",
        "03_TECHNICAL_DESIGN_DOCUMENT.md",
        "05_PROJECT_MANAGEMENT_PLAN.md",
        "06_QA_TEST_PLAN.md",
        "18_INDEPENDENT_PRODUCTION_READINESS_AUDIT.md",
    ]
    for rel in baseline_docs:
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        normalized = re.sub(r"[\s_-]+", "", text).lower()
        has_prelude = "前導" in text or "prelude" in normalized or "prechapter" in normalized or "pre章" in normalized
        has_chapter_1 = "第一章" in text or "chapter1" in normalized or "ch1" in normalized or "c1" in normalized
        if not has_prelude or not has_chapter_1:
            add(findings, "WARNING", "scope-baseline", rel, None, "Document does not explicitly mention both prelude/PRE and chapter 1/C1")

    tdd = (root / "03_TECHNICAL_DESIGN_DOCUMENT.md").read_text(encoding="utf-8") if (root / "03_TECHNICAL_DESIGN_DOCUMENT.md").is_file() else ""
    qa = qa_text
    asset = (root / "04_ASSET_LIST_AND_PRODUCTION_GUIDELINES.md").read_text(encoding="utf-8") if (root / "04_ASSET_LIST_AND_PRODUCTION_GUIDELINES.md").is_file() else ""
    for token in ["≤3 MB", "≤5 MB", "≤25 MB", "≤35 MB", "≤450k", "≤200", "≤512 MB"]:
        if token not in tdd:
            add(findings, "ERROR", "performance-baseline", "03_TECHNICAL_DESIGN_DOCUMENT.md", None, f"Missing baseline token {token}")
    for name, text in [("06_QA_TEST_PLAN.md", qa), ("04_ASSET_LIST_AND_PRODUCTION_GUIDELINES.md", asset)]:
        normalized = re.sub(r"\s+", "", text).lower()
        if "450k" not in normalized or "200" not in normalized or "35mb" not in normalized:
            add(findings, "WARNING", "performance-cross-doc", name, None, "Key performance budgets are not all repeated")

    # Source PDF integrity.
    pdf = root / "sources/TEAM-PDF-2026-INTRO.pdf"
    pdf_pages: int | None = None
    pdf_sha: str | None = None
    if pdf.is_file():
        pdf_sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
        if PdfReader is not None:
            try:
                pdf_pages = len(PdfReader(str(pdf)).pages)
                if pdf_pages != 5:
                    add(findings, "ERROR", "source-pdf", pdf.relative_to(root), None, f"Expected 5 pages; found {pdf_pages}")
            except Exception as exc:
                add(findings, "ERROR", "source-pdf", pdf.relative_to(root), None, f"Could not parse PDF: {exc}")
        else:
            add(findings, "WARNING", "source-pdf", pdf.relative_to(root), None, "pypdf unavailable; page count not checked")

    # File manifest integrity. MANIFEST.md and manifest.sha256 are intentionally
    # excluded to avoid recursive checksums.
    manifest_files: int | None = None
    manifest_bytes: int | None = None
    checksum_file = root / "manifest.sha256"
    manifest_excluded = {"MANIFEST.md", "manifest.sha256"}
    if checksum_file.is_file():
        listed: dict[str, str] = {}
        for lineno, raw in enumerate(checksum_file.read_text(encoding="utf-8").splitlines(), 1):
            if not raw.strip():
                continue
            match = re.fullmatch(r"([0-9a-fA-F]{64})\s{2}(.+)", raw)
            if not match:
                add(findings, "ERROR", "manifest-format", "manifest.sha256", lineno, "Expected '<sha256><two spaces><relative path>'")
                continue
            digest, rel = match.group(1).lower(), match.group(2)
            if rel in listed:
                add(findings, "ERROR", "manifest-duplicate", "manifest.sha256", lineno, f"Duplicate path: {rel}")
                continue
            listed[rel] = digest
            candidate = (root / rel).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                add(findings, "ERROR", "manifest-path", "manifest.sha256", lineno, f"Path leaves pack root: {rel}")
                continue
            if rel in manifest_excluded:
                add(findings, "ERROR", "manifest-recursion", "manifest.sha256", lineno, f"Manifest must exclude {rel}")
                continue
            if not candidate.is_file():
                add(findings, "ERROR", "manifest-missing", "manifest.sha256", lineno, f"Listed file does not exist: {rel}")
                continue
            actual = hashlib.sha256(candidate.read_bytes()).hexdigest()
            if actual != digest:
                add(findings, "ERROR", "manifest-hash", rel, None, f"Expected {digest}; found {actual}")

        expected = {
            path.relative_to(root).as_posix()
            for path in root.rglob("*")
            if path.is_file() and path.relative_to(root).as_posix() not in manifest_excluded
        }
        for rel in sorted(expected - set(listed)):
            add(findings, "ERROR", "manifest-unlisted", rel, None, "File is not listed in manifest.sha256")
        for rel in sorted(set(listed) - expected):
            add(findings, "ERROR", "manifest-extra", "manifest.sha256", None, f"Manifest lists unexpected path: {rel}")
        manifest_files = len(listed)
        manifest_bytes = sum((root / rel).stat().st_size for rel in listed if (root / rel).is_file())

    errors = sum(f.severity == "ERROR" for f in findings)
    warnings = sum(f.severity == "WARNING" for f in findings)
    result = Result(
        root=str(root),
        markdown_files=len(markdown),
        checked_links=checked_links,
        tables=table_count,
        qa_cases=len(qa_ids),
        decision_definitions=len(decision_ids),
        claim_definitions=len(claim_ids),
        source_pdf_pages=pdf_pages,
        source_pdf_sha256=pdf_sha,
        manifest_files=manifest_files,
        manifest_bytes=manifest_bytes,
        errors=errors,
        warnings=warnings,
        findings=findings,
    )

    if args.json:
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
    else:
        print(f"Root: {result.root}")
        print(f"Markdown files: {result.markdown_files}")
        print(f"Relative links checked: {result.checked_links}")
        print(f"Tables checked: {result.tables}")
        print(f"QA cases: {result.qa_cases}")
        print(f"Decision definitions: {result.decision_definitions}")
        print(f"Claim definitions: {result.claim_definitions}")
        print(f"Source PDF: {result.source_pdf_pages} pages; SHA-256 {result.source_pdf_sha256}")
        print(f"Manifest: {result.manifest_files} files; {result.manifest_bytes} bytes")
        print(f"Errors: {errors}; warnings: {warnings}")
        for finding in findings:
            location = f"{finding.file}:{finding.line}" if finding.line else finding.file
            print(f"[{finding.severity}] {finding.check} {location} — {finding.detail}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
