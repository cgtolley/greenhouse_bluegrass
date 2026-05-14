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
    font-family: "Courier New", Courier, monospace;
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
    width: 4em;
  }}
  td.key input {{
    font-family: "Courier New", Courier, monospace;
    font-size: 0.95rem;
    color: {accent_color};
    font-weight: bold;
    width: 3.2em;
    padding: 0.15rem 0.3rem;
    border: 1px solid #ddd;
    border-radius: 3px;
    background: #fafafa;
  }}
  td.key input.invalid {{
    border-color: #c44;
    background: #fff0f0;
  }}
  td.key input.changed {{
    border-color: {accent_color};
    background: #fff;
  }}
  td.sources {{
    font-size: 0.85rem;
  }}
  td.artist {{
    font-style: italic;
    color: #555;
    font-size: 0.9rem;
  }}
  td.listen {{
    text-align: center;
    width: 2.5em;
  }}
  td.listen a {{
    font-size: 1.1rem;
    text-decoration: none;
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
  #song-search {{
    font-family: inherit;
    font-size: 1rem;
    width: 100%;
    padding: 0.5rem 0.7rem;
    margin-bottom: 1rem;
    border: 1px solid #ddd;
    border-radius: 3px;
    background: #fafafa;
    box-sizing: border-box;
  }}
  #song-search:focus {{
    outline: none;
    border-color: {accent_color};
    background: #fff;
  }}
  .no-results {{
    color: #aaa;
    font-style: italic;
    margin-top: 1rem;
    display: none;
  }}
  .no-results.visible {{
    display: block;
  }}
</style>
</head>
<body>

<h1>{site_title}</h1>

<input type="search" id="song-search" placeholder="Search by song or artist…" autocomplete="off" />
<p class="no-results">No songs match your search.</p>

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
        key = s["key"]
        artist = s.get("artist") or ""
        listen_url = s.get("listen") or ""
        artist_cell = esc(artist) if artist else "&mdash;"
        listen_cell = (
            f'<a href="{esc(listen_url)}" aria-label="Listen" title="Listen">▶</a>'
            if listen_url else "&mdash;"
        )
        rows.append(
            "    <tr>\n"
            f'      <td><a class="song-link" href="{esc(s["file"])}" data-base="{esc(s["file"])}">{esc(s["title"])}</a></td>\n'
            f'      <td class="artist">{artist_cell}</td>\n'
            f'      <td class="key"><input type="text" class="key-input" value="{esc(key)}" data-original="{esc(key)}" maxlength="4" aria-label="Transpose key" /></td>\n'
            f'      <td class="listen">{listen_cell}</td>\n'
            f'      <td class="sources">{render_sources(s.get("sources", []))}</td>\n'
            "    </tr>"
        )
    table_html = (
        "<table>\n"
        "  <thead>\n"
        "    <tr><th>Song</th><th>Artist</th><th>Key</th><th>Listen</th><th>Sources</th></tr>\n"
        "  </thead>\n"
        "  <tbody>\n"
        + "\n".join(rows) + "\n"
        "  </tbody>\n"
        "</table>"
    )
    return table_html + INDEX_SCRIPT


INDEX_SCRIPT = """

<script>
(function () {
  var VALID = {
    // Majors
    "C":1,"C#":1,"Db":1,"D":1,"D#":1,"Eb":1,"E":1,"F":1,"F#":1,"Gb":1,
    "G":1,"G#":1,"Ab":1,"A":1,"A#":1,"Bb":1,"B":1,
    // Minors (both spellings of enharmonic ones accepted)
    "Cm":1,"C#m":1,"Dbm":1,"Dm":1,"D#m":1,"Ebm":1,"Em":1,"Fm":1,"F#m":1,
    "Gbm":1,"Gm":1,"G#m":1,"Abm":1,"Am":1,"A#m":1,"Bbm":1,"Bm":1
  };

  function normalize(v) {
    if (v.length === 0) return v;
    // Capitalize first letter only; lowercase the rest (so "ebm" -> "Ebm", "F#M" -> "F#m")
    return v[0].toUpperCase() + v.slice(1).toLowerCase();
  }

  document.querySelectorAll(".key-input").forEach(function (input) {
    var link = input.closest("tr").querySelector(".song-link");
    var base = link.getAttribute("data-base");
    var original = input.getAttribute("data-original");

    function update() {
      var v = normalize(input.value.trim());

      input.classList.toggle("invalid", v.length > 0 && !(v in VALID));
      input.classList.toggle("changed", v in VALID && v !== original);

      if (v in VALID && v !== original) {
        link.href = base + "?key=" + encodeURIComponent(v);
      } else {
        link.href = base;
      }
    }

    input.addEventListener("input", update);
    input.addEventListener("blur", function () {
      // Tidy display: normalize as user leaves the field
      var v = input.value.trim();
      if (v.length > 0) input.value = normalize(v);
    });
  });

  // --- Search filter ---
  var search = document.getElementById("song-search");
  var rows = document.querySelectorAll("tbody tr");
  var noResults = document.querySelector(".no-results");

  if (search) {
    search.addEventListener("input", function () {
      var q = search.value.trim().toLowerCase();
      var anyVisible = false;
      rows.forEach(function (row) {
        var titleEl = row.querySelector(".song-link");
        var artistEl = row.querySelector(".artist");
        var title = titleEl ? titleEl.textContent.toLowerCase() : "";
        var artist = artistEl ? artistEl.textContent.toLowerCase() : "";
        var match = !q || title.indexOf(q) !== -1 || artist.indexOf(q) !== -1;
        row.style.display = match ? "" : "none";
        if (match) anyVisible = true;
      });
      if (noResults) noResults.classList.toggle("visible", !anyVisible && q.length > 0);
    });
  }
})();
</script>
"""


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
        "--color", default="#363",
        help="base accent color (default: #363)",
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
