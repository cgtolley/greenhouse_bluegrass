#!/usr/bin/env python3
"""
render_song.py — Render a Nashville-notation song JSON to HTML in a chosen key.

Usage:
    python render_song.py SONG_FILE KEY [-o OUTPUT_FILE] [--color HEX]

Examples:
    python render_song.py songs/example.json G
    python render_song.py songs/example.json Eb -o example_Eb.html
    python render_song.py songs/example.json D --color "#1a8"

The song file is a JSON document. See song_template.json for the format.

Color resolution order:
    1. --color CLI argument (if given)
    2. "color" field in the song JSON (if present)
    3. Default: "#b54"
"""

import argparse
import colorsys
import html as htmllib
import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Music theory
# ---------------------------------------------------------------------------

NOTES_SHARP = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
NOTES_FLAT  = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

KEY_TO_SEMITONE = {
    "C": 0,  "C#": 1, "Db": 1, "D": 2,  "D#": 3, "Eb": 3,
    "E": 4,  "F": 5,  "F#": 6, "Gb": 6, "G": 7,  "G#": 8, "Ab": 8,
    "A": 9,  "A#": 10, "Bb": 10, "B": 11,
}

FLAT_KEYS = {"F", "Bb", "Eb", "Ab", "Db", "Gb"}
SCALE_DEGREE_SEMITONES = {1: 0, 2: 2, 3: 4, 4: 5, 5: 7, 6: 9, 7: 11}

CHORD_RE = re.compile(
    r"(?<![A-Za-z0-9])"
    r"(?P<acc>[b#])?"
    r"(?P<deg>[1-7])"
    r"(?P<qual>m(?!aj)|maj|dim|aug|sus[24]?)?"
    r"(?P<ext>7|9|11|13)?"
    r"(?:/(?P<bass_acc>[b#])?(?P<bass>[1-7]))?"
    r"(?![A-Za-z0-9])"
)


def note_at(key, semitone_offset, prefer_flats=None):
    if prefer_flats is None:
        prefer_flats = key in FLAT_KEYS
    idx = (KEY_TO_SEMITONE[key] + semitone_offset) % 12
    return (NOTES_FLAT if prefer_flats else NOTES_SHARP)[idx]


def transpose_chord_match(match, key):
    deg = int(match.group("deg"))
    offset = SCALE_DEGREE_SEMITONES[deg]
    acc = match.group("acc")
    if acc == "b":
        offset -= 1
        prefer_flats = True
    elif acc == "#":
        offset += 1
        prefer_flats = False
    else:
        prefer_flats = None

    root = note_at(key, offset, prefer_flats)
    out = root
    if match.group("qual"):
        out += match.group("qual")
    if match.group("ext"):
        out += match.group("ext")

    bass_deg = match.group("bass")
    if bass_deg:
        bass_offset = SCALE_DEGREE_SEMITONES[int(bass_deg)]
        bass_acc = match.group("bass_acc")
        if bass_acc == "b":
            bass_offset -= 1
            bass_prefer_flats = True
        elif bass_acc == "#":
            bass_offset += 1
            bass_prefer_flats = False
        else:
            bass_prefer_flats = prefer_flats
        out += "/" + note_at(key, bass_offset, bass_prefer_flats)

    return out


def transpose_chord_row(chord_row, key):
    chars = list(chord_row)
    for m in CHORD_RE.finditer(chord_row):
        start = m.start()
        new = transpose_chord_match(m, key)
        for j, ch in enumerate(new):
            if start + j < len(chars):
                chars[start + j] = ch
            else:
                chars.append(ch)
        old_len = m.end() - m.start()
        if len(new) < old_len:
            for j in range(len(new), old_len):
                chars[start + j] = " "
    return "".join(chars).rstrip()


# ---------------------------------------------------------------------------
# Color palette
# ---------------------------------------------------------------------------

TITLE_LIGHTNESS = 0.22
CHORD_LIGHTNESS = 0.48
DEFAULT_COLOR = "#b54"


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
    chord_rgb = colorsys.hls_to_rgb(h, CHORD_LIGHTNESS, s)
    return rgb_to_hex(title_rgb), rgb_to_hex(chord_rgb)


# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  html {{
    font-size: clamp(13px, 3.2vw, 16px);
  }}
  body {{
    font-family: "Courier New", Courier, monospace;
    max-width: 720px;
    padding: 0 1rem;
    margin: 1.1rem auto;
    color: #222;
    line-height: 1.4;
  }}
  h2 {{
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #888;
    margin-top: 0.1rem;
    margin-bottom: 0.1rem;
  }}
  h1 {{
    font-size: 1rem;
    letter-spacing: 0.1em;
    color: {title_color};
    border-bottom: 1px solid #ddd;
    padding-bottom: 0.25rem;
    margin-top: 0.5rem;
    margin-bottom: 0.25rem;
  }}
  .key {{
    font-size: 0.8rem;
    color: #888;
    margin-bottom: 0.75rem;
  }}
  .key select {{
    font-family: inherit;
    font-size: inherit;
    color: {chord_color};
    background: transparent;
    border: 1px solid #ddd;
    border-radius: 3px;
    padding: 0 0.2rem;
    margin-left: 0.3rem;
    font-weight: bold;
  }}
  pre.lyrics {{
    font-family: "Courier New", Courier, monospace;
    /* Scaled so the longest line ({longest_line} chars) fits the available width.
       0.62 ≈ Courier New character-width / font-size ratio (small safety margin).
       Worst-case length across all keys, so transposing live never overflows. */
    font-size: clamp(0.4rem, calc((100vw - 2rem) / {longest_line} / 0.62), 0.95rem);
    line-height: 1.4;
    margin: 0;
    white-space: pre;
  }}
  pre.lyrics .chord {{
    color: {chord_color};
    font-weight: bold;
  }}
</style>
</head>
<body data-default-key="{key}">

<h1>{title}</h1>
<div class="key">Key of <select id="key-selector" aria-label="Transpose to key">{key_options}</select></div>

{sections}

<script>
(function () {{
  var NOTES_SHARP = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"];
  var NOTES_FLAT  = ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"];
  var KEY_TO_SEMITONE = {{"C":0,"C#":1,"Db":1,"D":2,"D#":3,"Eb":3,"E":4,"F":5,"F#":6,"Gb":6,"G":7,"G#":8,"Ab":8,"A":9,"A#":10,"Bb":10,"B":11}};
  var FLAT_KEYS = {{"F":1,"Bb":1,"Eb":1,"Ab":1,"Db":1,"Gb":1}};
  var SDS = {{1:0,2:2,3:4,4:5,5:7,6:9,7:11}};
  var CHORD_RE = /(?<![A-Za-z0-9])([b#])?([1-7])(m(?!aj)|maj|dim|aug|sus[24]?)?(7|9|11|13)?(?:\\/([b#])?([1-7]))?(?![A-Za-z0-9])/g;

  function noteAt(key, offset, preferFlats) {{
    if (preferFlats === null) preferFlats = !!FLAT_KEYS[key];
    var idx = ((KEY_TO_SEMITONE[key] + offset) % 12 + 12) % 12;
    return preferFlats ? NOTES_FLAT[idx] : NOTES_SHARP[idx];
  }}

  function transposeChord(m, key) {{
    var acc = m[1], degStr = m[2], qual = m[3], ext = m[4], bassAcc = m[5], bassStr = m[6];
    var offset = SDS[parseInt(degStr, 10)];
    var pf = null;
    if (acc === "b") {{ offset--; pf = true; }}
    else if (acc === "#") {{ offset++; pf = false; }}
    var out = noteAt(key, offset, pf);
    if (qual) out += qual;
    if (ext) out += ext;
    if (bassStr) {{
      var bo = SDS[parseInt(bassStr, 10)];
      var bpf = pf;
      if (bassAcc === "b") {{ bo--; bpf = true; }}
      else if (bassAcc === "#") {{ bo++; bpf = false; }}
      out += "/" + noteAt(key, bo, bpf);
    }}
    return out;
  }}

  function transposeRow(row, key) {{
    var chars = row.split("");
    var re = new RegExp(CHORD_RE.source, "g");
    var m;
    while ((m = re.exec(row)) !== null) {{
      var start = m.index;
      var newChord = transposeChord(m, key);
      for (var j = 0; j < newChord.length; j++) {{
        if (start + j < chars.length) chars[start + j] = newChord[j];
        else chars.push(newChord[j]);
      }}
      var oldLen = m[0].length;
      if (newChord.length < oldLen) {{
        for (var k = newChord.length; k < oldLen; k++) chars[start + k] = " ";
      }}
    }}
    return chars.join("").replace(/\\s+$/, "");
  }}

  function rerender(key) {{
    var spans = document.querySelectorAll(".chord[data-nash]");
    if (key === "Nashville") {{
      for (var i = 0; i < spans.length; i++) {{
        spans[i].textContent = spans[i].dataset.nash.replace(/\\s+$/, "");
      }}
    }} else if (key in KEY_TO_SEMITONE) {{
      for (var i = 0; i < spans.length; i++) {{
        spans[i].textContent = transposeRow(spans[i].dataset.nash, key);
      }}
    }} else {{
      return false;
    }}
    var sel = document.getElementById("key-selector");
    if (sel && sel.value !== key) sel.value = key;
    return true;
  }}

  var params = new URLSearchParams(window.location.search);
  var urlKey = params.get("key");
  if (urlKey && (urlKey === "Nashville" || urlKey in KEY_TO_SEMITONE)) rerender(urlKey);

  var sel = document.getElementById("key-selector");
  if (sel) sel.addEventListener("change", function () {{ rerender(sel.value); }});
}})();
</script>

</body>
</html>
"""


def esc(s):
    return htmllib.escape(s) if s else ""


def render_section(section, key):
    label = section.get("label", section["type"].title())
    blocks = []
    for line in section["lines"]:
        chord_row, lyric_row = line[0], line[1] if len(line) > 1 else None
        chord_html = esc(transpose_chord_row(chord_row, key))
        nash_attr = esc(chord_row)
        if lyric_row:
            blocks.append(
                f'<span class="chord" data-nash="{nash_attr}">{chord_html}</span>\n{esc(lyric_row)}'
            )
        else:
            blocks.append(
                f'<span class="chord" data-nash="{nash_attr}">{chord_html}</span>'
            )
    body = "\n".join(blocks)
    return f'<h2>{esc(label)}</h2>\n<pre class="lyrics">\n{body}\n</pre>\n'


def compute_longest_line(song):
    """Worst-case line width across all 12 keys, so the CSS-baked font size
    accommodates any live JS transposition."""
    longest = 1
    for section in song["sections"]:
        for line in section["lines"]:
            chord_row = line[0]
            lyric_row = line[1] if len(line) > 1 else None
            if lyric_row:
                longest = max(longest, len(lyric_row))
            for k in KEY_TO_SEMITONE:
                longest = max(longest, len(transpose_chord_row(chord_row, k)))
    return longest


KEY_ORDER = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def render_key_options(current_key):
    options = ['<option value="Nashville">Nashville</option>']
    for k in KEY_ORDER:
        selected = " selected" if k == current_key else ""
        options.append(f'<option value="{k}"{selected}>{k}</option>')
    if current_key not in KEY_ORDER and current_key != "Nashville":
        options.insert(1, f'<option value="{current_key}" selected>{current_key}</option>')
    return "".join(options)


def render_song(song, key, title_color, chord_color):
    sections_html = "\n".join(render_section(s, key) for s in song["sections"])
    return HTML_TEMPLATE.format(
        title=esc(song["title"]),
        key=esc(key),
        key_options=render_key_options(key),
        title_color=title_color,
        chord_color=chord_color,
        longest_line=compute_longest_line(song),
        sections=sections_html,
    )


def load_song(path):
    try:
        text = Path(path).read_text()
    except OSError as e:
        sys.exit(f"Could not open {path}: {e}")
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        sys.exit(f"Invalid JSON in {path}: {e}")
    for required in ("title", "sections"):
        if required not in data:
            sys.exit(f"{path} is missing required field: {required!r}")
    return data


def update_manifest(output_path, song, key, manifest_path="songs.json"):
    """Add or update this song's entry in songs.json, matched by file path."""
    path = Path(manifest_path)
    if path.exists():
        data = json.loads(path.read_text())
    else:
        data = {"site_title": "Songbook", "songs": []}

    entry = {
        "title": song["title"],
        "key": key,
        "file": output_path,
        "sources": song.get("sources", []),
    }

    songs = data.setdefault("songs", [])
    for i, existing in enumerate(songs):
        if existing.get("file") == output_path:
            songs[i] = entry
            break
    else:
        songs.append(entry)

    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Updated {manifest_path}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Render a Nashville-notation song JSON to HTML in any key."
    )
    parser.add_argument("song", help="path to a song .json file")
    parser.add_argument("key", help="target key, e.g. C, G, Eb, F#")
    parser.add_argument("-o", "--output", help="output HTML file (default: stdout)")
    parser.add_argument(
        "--color",
        default=None,
        help='base hex color (e.g. "#b54"). Overrides the "color" field in the '
             'song JSON. If neither is set, defaults to "#b54".',
    )
    args = parser.parse_args()

    if args.key not in KEY_TO_SEMITONE:
        sys.exit(
            f"Unknown key: {args.key}\n"
            f"Valid keys: {', '.join(sorted(KEY_TO_SEMITONE))}"
        )

    song = load_song(args.song)

    # Color: CLI flag > song JSON > default
    color = args.color or song.get("color") or DEFAULT_COLOR
    try:
        title_color, chord_color = derive_palette(color)
    except ValueError as e:
        sys.exit(str(e))

    out = render_song(song, args.key, title_color, chord_color)

    if args.output:
        Path(args.output).write_text(out)
        print(f"Wrote {args.output} (color {color} → title {title_color}, chord {chord_color})",
              file=sys.stderr)
        update_manifest(args.output, song, args.key)
    else:
        print(out)


if __name__ == "__main__":
    main()
