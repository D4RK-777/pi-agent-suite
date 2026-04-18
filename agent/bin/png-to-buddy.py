#!/usr/bin/env python3
"""
png-to-buddy.py
Converts a small PNG pixel-art sprite to TypeScript byte-buddy frame format.

Uses Unicode half-block chars (▀ ▄ █ space) for 2× vertical resolution:
  top-only pixel  → ▀  (upper half block)
  bottom-only     → ▄  (lower half block)
  both pixels     → █  (full block)
  neither         → space

Pixels with alpha < 128 are treated as transparent (space).

Usage:
  python png-to-buddy.py <sprite.png>
  python png-to-buddy.py <sprite.png> --no-colors     # monochrome output
  python png-to-buddy.py <sprite.png> --256           # ANSI 256-color mode
  python png-to-buddy.py <sprite.png> --preview-only  # just render, no TS output

Designed for the byte-buddy extension in pi-coding-agent.
Output can be pasted directly into the `frames` map in byte-buddy.ts.
"""

import sys
import os
from PIL import Image

# Force UTF-8 output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RESET = "\x1b[0m"

# ── ANSI 16-color palette ─────────────────────────────────────────────────────
# (code, R, G, B, name) — approximate terminal RGB for nearest-match
ANSI16 = [
    ("\x1b[30m",   0,   0,   0, "black"),
    ("\x1b[31m", 170,   0,   0, "red"),
    ("\x1b[32m",   0, 170,   0, "green"),
    ("\x1b[33m", 170,  85,   0, "dark-yellow"),
    ("\x1b[34m",   0,   0, 170, "blue"),
    ("\x1b[35m", 170,   0, 170, "magenta"),
    ("\x1b[36m",   0, 170, 170, "cyan"),
    ("\x1b[37m", 170, 170, 170, "white"),
    ("\x1b[90m",  85,  85,  85, "bright-black"),
    ("\x1b[91m", 255,  85,  85, "bright-red"),
    ("\x1b[92m",  85, 255,  85, "bright-green"),
    ("\x1b[93m", 255, 255,  85, "bright-yellow"),
    ("\x1b[94m",  85,  85, 255, "bright-blue"),
    ("\x1b[95m", 255,  85, 255, "bright-magenta"),
    ("\x1b[96m",  85, 255, 255, "bright-cyan"),
    ("\x1b[97m", 255, 255, 255, "bright-white"),
]


def nearest_ansi16(r, g, b):
    best_code, best_dist = ANSI16[0][0], float("inf")
    for code, cr, cg, cb, _ in ANSI16:
        d = (r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2
        if d < best_dist:
            best_dist = d
            best_code = code
    return best_code


def ansi256_fg(r, g, b):
    """Map RGB to closest ANSI 256-color foreground code."""
    # 6×6×6 color cube (indices 16–231)
    ri = round(r / 255 * 5)
    gi = round(g / 255 * 5)
    bi = round(b / 255 * 5)
    idx = 16 + 36 * ri + 6 * gi + bi
    return f"\x1b[38;5;{idx}m"


def color_code(r, g, b, use_256):
    return ansi256_fg(r, g, b) if use_256 else nearest_ansi16(r, g, b)


def convert(img_path, use_colors=True, use_256=False):
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    pixels = img.load()

    rows = []

    for row_pair in range(0, h, 2):
        y_top = row_pair
        y_bot = row_pair + 1 if row_pair + 1 < h else None

        line = ""
        cur_color = ""

        for x in range(w):
            tr, tg, tb, ta = pixels[x, y_top]
            top_on = ta >= 128

            if y_bot is not None:
                br, bg, bb, ba = pixels[x, y_bot]
                bot_on = ba >= 128
            else:
                br, bg, bb, ba = 0, 0, 0, 0
                bot_on = False

            if not top_on and not bot_on:
                char = " "
                col = ""
            elif top_on and bot_on:
                char = "█"
                col = color_code(tr, tg, tb, use_256) if use_colors else ""
            elif top_on:
                char = "▀"
                col = color_code(tr, tg, tb, use_256) if use_colors else ""
            else:
                char = "▄"
                col = color_code(br, bg, bb, use_256) if use_colors else ""

            if use_colors and col != cur_color:
                if cur_color:
                    line += RESET
                if col:
                    line += col
                cur_color = col

            line += char

        if cur_color:
            line += RESET

        rows.append(line)

    return rows, w, (h + 1) // 2


def escape_for_ts(s):
    """Escape a string for use in a TypeScript template literal."""
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")


def main():
    args = sys.argv[1:]

    if not args or args[0].startswith("--"):
        print(__doc__)
        sys.exit(1)

    img_path = args[0]
    use_colors = "--no-colors" not in args
    use_256 = "--256" in args
    preview_only = "--preview-only" in args

    if not os.path.isfile(img_path):
        print(f"Error: file not found: {img_path}", file=sys.stderr)
        sys.exit(1)

    rows, char_width, char_height = convert(img_path, use_colors, use_256)

    # ── terminal preview ──────────────────────────────────────────────────────
    print(f"\n── Preview ({char_width}w × {char_height}h terminal chars) ──")
    for row in rows:
        print(row)
    print()

    if preview_only:
        return

    # ── TypeScript output ─────────────────────────────────────────────────────
    print("── TypeScript frame array (paste into byte-buddy.ts) ──")
    print()
    print("const frame: string[] = [")
    for row in rows:
        escaped = escape_for_ts(row)
        print(f"  `{escaped}`,")
    print("];")
    print()

    # ── monochrome guide (for hand-coloring with ANSI helpers) ───────────────
    if use_colors:
        mono_rows, _, _ = convert(img_path, use_colors=False)
        print("── Monochrome shape (for hand-coloring with line()/eyeRow() helpers) ──")
        for row in mono_rows:
            # Print with visible spaces
            print(repr(row))
        print()

    print("── Char palette used ──")
    print("  █  full block   — both pixels filled")
    print("  ▀  upper half   — top pixel only")
    print("  ▄  lower half   — bottom pixel only")
    print("  (space)         — transparent / background")
    print()
    print("  Tip: swap ▒ for █ in blink frames for the dotted-eye effect.")


if __name__ == "__main__":
    main()
