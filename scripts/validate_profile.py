#!/usr/bin/env python3
"""Offline structural checks for the GitHub profile README (stdlib only)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / 'README.md'
EXPECTED_REPOS = (
    'VietLex-Tech-Spec',
    'CV-Review-System',
    'finevent-nlp-finance',
    'vaipe-medguard',
    'YoutubeAgents',
    'NEU-Surface-Defect-Detection',
)


def validate(text: str) -> list[str]:
    errors: list[str] = []
    if not text.startswith('# '):
        errors.append('README must begin with a Markdown H1 heading')
    if re.search(r'</?[a-z][^>]*>', text, re.IGNORECASE):
        errors.append('Avoid inline HTML; use plain GitHub Flavored Markdown')

    opening: tuple[str, int] | None = None
    for number, line in enumerate(text.splitlines(), start=1):
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if not match:
            continue
        marker = match.group(1)
        current = (marker[0], len(marker))
        if opening is None:
            opening = current
        elif current[0] == opening[0] and current[1] >= opening[1]:
            opening = None
    if opening is not None:
        errors.append('Unclosed Markdown code fence')

    links = re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', text)
    if text.count('](') != len(links):
        errors.append('Potentially malformed Markdown link syntax')
    for link in links:
        if link.startswith('https://'):
            continue
        if link.startswith('#'):
            continue
        if not link.startswith(('http://', 'mailto:', 'javascript:')):
            if not (ROOT / link.split('#', 1)[0]).exists():
                errors.append(f'Missing local link target: {link}')
        else:
            errors.append(f'Non-HTTPS or unsupported link target: {link}')

    for name in EXPECTED_REPOS:
        expected = f'https://github.com/TanNguyen234/{name}'
        if expected not in links:
            errors.append(f'Missing featured project link: {expected}')

    if re.search(r'!\[[^\]]*\]\(https?://', text):
        errors.append('External images can fail independently of GitHub; remove or review them')
    return errors


def main() -> int:
    if not README.exists():
        print('FAIL: README.md is missing')
        return 1
    text = README.read_text(encoding='utf-8')
    issues = validate(text)
    if issues:
        for issue in issues:
            print(f'FAIL: {issue}')
        return 1
    print('PASS: profile Markdown structure, links, and expected project references')
    print('NOTE: live URLs, claims, and rendered layout still require manual verification')
    return 0


if __name__ == '__main__':
    sys.exit(main())
