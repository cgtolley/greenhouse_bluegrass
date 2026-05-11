#!/usr/bin/env python3
"""
render_index.py — Generate index.html from songs.json.

The manifest songs.json is maintained automatically by render_song.py;
this script reads it and emits a homepage with a table of all songs.

Usage:
    python render_index.py
    python render_index.py -o index.html
    python render_index.py --color "#3a3"
"""

import argparse
import colorsys
import html as htmllib
import json
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Color palette (mirrors render_song.py so the index matches the song pages)
# ---------------------------------------------------------------------------

TITLE_LIGHTNESS = 0.22
ACCENT_LIGHTNESS = 0.48


def parse_hex_color(s):
    s = s.lstrip("#").strip()
    if len(s) == 3:
        s = "".join(c * 2 for c in s)
    if len(s) != 6 or not all(c in "0123456789abcdefABCDEF" for c in s):
        raise ValueError(f"Not a valid hex color: {s!r}")
    return tuple(int(s[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{max(0, min(255, round(c * 255))):02x}" for c in rgb)


def derive_palette(base_hex):
    r, g, b = parse_hex_color(base_hex)
    h, _l, s = colorsys.rgb_to_hls(r, g, b)
    title_rgb = colorsys.hls_to_rgb(h, TITLE_LIGHTNESS, s)
    accent_rgb = colorsys.hls_to_rgb(h, ACCENT_LIGHTNESS, s)
    return rgb_to_hex(title_rgb), rgb_to_hex(accent_rgb)


# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{site_title}</title>
<style>
  html {{
    font-size: clamp(13px, 3.2vw, 16px);
  }}
  body {{
    font-family: Georgia, "Times New Roman", serif;
    max-width: 720px;
    padding: 0 1rem;
    margin: 1.5rem auto;
    color: #222;
    line-height: 1.5;
  }}
  h1 {{
    font-size: 1.6rem;
    letter-spacing: 0.04em;
    color: {title_color};
    border-bottom: 1px solid #ddd;
    padding-bottom: 0.4rem;
    margin-bottom: 1rem;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
  }}
  th, td {{
    text-align: left;
    padding: 0.5rem 0.6rem;
    border-bottom: 1px solid #eee;
    vertical-align: top;
  }}
  th {{
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #888;
    font-weight: normal;
    border-bottom: 1px solid #ddd;
  }}
  td.key {{
    font-family: "Courier New", Courier, monospace;
    color: {accent_color};
    font-weight: bold;
    width: 3em;
  }}
  td.sources {{
    font-size: 0.85rem;
  }}
  a {{
    color: {accent_color};
    text-decoration: none;
  }}
  a:hover {{
    text-decoration: underline;
  }}
  .empty {{
    color: #aaa;
    font-style: italic;
    margin-top: 1rem;
  }}
</style>
</head>
<body>

<h1>{site_title}</h1>

{table}

</body>
</html>
"""


def esc(s):
    return htmllib.escape(s) if s else ""


def render_sources(sources):
    if not sources:
        return "&mdash;"
    parts = []
    for src in sources:
        # Accept either [name, url] or {"name": ..., "url": ...}
        if isinstance(src, dict):
            name, url = src.get("name", "source"), src.get("url", "#")
        else:
            name, url = src[0], src[1]
        parts.append(f'<a href="{esc(url)}">{esc(name)}</a>')
    return ", ".join(parts)


def render_table(songs):
    if not songs:
        return '<p class="empty">No songs yet. Run render_song.py to add one.</p>'
    rows = []
    for s in songs:
        rows.append(
            "    <tr>\n"
            f'      <td><a href="{esc(s["file"])}">{esc(s["title"])}</a></td>\n'
            f'      <td class="key">{esc(s["key"])}</td>\n'
            f'      <td class="sources">{render_sources(s.get("sources", []))}</td>\n'
            "    </tr>"
        )
    return (
        "<table>\n"
        "  <thead>\n"
        "    <tr><th>Song</th><th>Key</th><th>Sources</th></tr>\n"
        "  </thead>\n"
        "  <tbody>\n"
        + "\n".join(rows) + "\n"
        "  </tbody>\n"
        "</table>"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Generate index.html from songs.json."
    )
    parser.add_argument(
        "-m", "--manifest", default="songs.json",
        help="manifest file (default: songs.json)",
    )
    parser.add_argument(
        "-o", "--output", default="index.html",
        help="output HTML file (default: index.html)",
    )
    parser.add_argument(
        "--color", default="#b54",
        help="base accent color (default: #b54)",
    )
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        sys.exit(
            f"Manifest not found: {args.manifest}\n"
            f"Render a song first (it creates the manifest), or create the file by hand."
        )

    data = json.loads(manifest_path.read_text())
    site_title = data.get("site_title", "Songbook")
    songs = data.get("songs", [])

    try:
        title_color, accent_color = derive_palette(args.color)
    except ValueError as e:
        sys.exit(str(e))

    html = HTML_TEMPLATE.format(
        site_title=esc(site_title),
        title_color=title_color,
        accent_color=accent_color,
        table=render_table(songs),
    )

    Path(args.output).write_text(html)
    print(f"Wrote {args.output} with {len(songs)} song(s)", file=sys.stderr)


if __name__ == "__main__":
    main()
