#!/usr/bin/env python3
"""Find hardcoded design values in front-end source.

Usage: find_hardcoded.py <dir> [--ext tsx,jsx,ts,js,css,scss,astro,vue,svelte,html]

Prints  kind  file:line  value  |  source line
Exit code 0 always; this is a report, not a gate.
"""
import os
import re
import sys

DEFAULT_EXT = "tsx,jsx,ts,js,css,scss,astro,vue,svelte,html,mdx"
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".astro", "out", "coverage", "public"}
# Files that *define* tokens are allowed to contain literals.
TOKEN_FILE_HINTS = ("token", "theme", "tailwind.config", "global.css", "globals.css", "variables", "design-system")

PATTERNS = {
    "color-hex": re.compile(r"(?<![\w-])#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b"),
    "color-fn": re.compile(r"\b(?:rgba?|hsla?|oklch|oklab)\([^)]*\)"),
    "px-spacing": re.compile(r"\b(?:margin|padding|gap|top|right|bottom|left|inset|width|height|max-width|min-width)[a-z-]*\s*:\s*-?\d+(?:\.\d+)?px"),
    "tailwind-arbitrary": re.compile(r"\b(?:[a-z]+:)?(?:p|m|px|py|mx|my|pt|pb|pl|pr|mt|mb|ml|mr|gap|w|h|text|rounded|shadow|top|left|right|bottom|inset|z)-\[[^\]]+\]"),
    "font-size": re.compile(r"\bfont-size\s*:\s*\d+(?:\.\d+)?(?:px|rem|em|pt)"),
    "font-family": re.compile(r"\bfont-family\s*:\s*[^;]+"),
    "radius": re.compile(r"\bborder-radius\s*:\s*\d+(?:\.\d+)?(?:px|rem|%)"),
    "shadow": re.compile(r"\bbox-shadow\s*:\s*[^;]+"),
    "z-index": re.compile(r"\bz-index\s*:\s*\d+"),
    "inline-style": re.compile(r"\bstyle=\{\{|\bstyle=\"[^\"]*(?:color|padding|margin|font)[^\"]*\""),
}

# Things that look like literals but are almost always fine.
ALLOW = re.compile(r"var\(--|\$\{|currentColor|transparent|inherit|0px\b|100%|url\(")


def is_token_file(path: str) -> bool:
    low = path.lower()
    return any(h in low for h in TOKEN_FILE_HINTS)


def scan(root: str, exts: set[str]):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.rsplit(".", 1)[-1] not in exts:
                continue
            path = os.path.join(dirpath, fn)
            if is_token_file(path):
                continue
            try:
                with open(path, encoding="utf-8", errors="ignore") as f:
                    for n, line in enumerate(f, 1):
                        s = line.strip()
                        if not s or s.startswith(("//", "*", "/*", "#")):
                            continue
                        for kind, rx in PATTERNS.items():
                            for m in rx.finditer(line):
                                val = m.group(0)
                                if ALLOW.search(val):
                                    continue
                                yield kind, f"{path}:{n}", val, s[:120]
            except OSError:
                continue


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)
    root = args[0]
    exts = DEFAULT_EXT
    if "--ext" in args:
        exts = args[args.index("--ext") + 1]
    exts = set(exts.split(","))

    counts: dict[str, int] = {}
    rows = list(scan(root, exts))
    for kind, loc, val, src in rows:
        counts[kind] = counts.get(kind, 0) + 1
        print(f"{kind:18} {loc:48} {val:40} | {src}")

    print("\n== summary ==")
    for kind, c in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"{c:5}  {kind}")
    print(f"{len(rows):5}  total")


if __name__ == "__main__":
    main()
