#!/usr/bin/env python3
"""
render_song.py — Render a Nashville-notation song file to HTML in a chosen key.

Usage:
    python render_song.py SONG_FILE KEY [-o OUTPUT_FILE]

Examples:
    python render_song.py songs/example.py G
    python render_song.py songs/example.py Eb -o example_Eb.html

The song file should be a Python module that defines a SONG dict.
See song_template.py for the format.
"""

import argparse
import importlib.util
import html as htmllib
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

# Keys that conventionally spell notes with flats.
FLAT_KEYS = {"F", "Bb", "Eb", "Ab", "Db", "Gb"}

# Major-scale semitone offsets from the tonic, for degrees 1–7.
SCALE_DEGREE_SEMITONES = {1: 0, 2: 2, 3: 4, 4: 5, 5: 7, 6: 9, 7: 11}

# Pattern matching a Nashville chord symbol embedded in any context.
# Examples it matches: 1, 5m, 6m, 57, 1maj7, 5/7, 1sus4, b3, #4
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
    """Return the note name `semitone_offset` semitones above `key`."""
    if prefer_flats is None:
        prefer_flats = key in FLAT_KEYS
    idx = (KEY_TO_SEMITONE[key] + semitone_offset) % 12
    return (NOTES_FLAT if prefer_flats else NOTES_SHARP)[idx]


def transpose_chord_match(match, key):
    """Given a regex match for a Nashville chord, return the chord name in `key`."""
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
        prefer_flats = None  # follow key default

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
    """Replace each Nashville chord in `chord_row` with its name in `key`,
    preserving each chord's source column. If a transposed chord is longer
    than the original token, it overwrites following space characters."""
    chars = list(chord_row)
    for m in CHORD_RE.finditer(chord_row):
        start = m.start()
        new = transpose_chord_match(m, key)
        # Write new chars at the source position
        for j, ch in enumerate(new):
            if start + j < len(chars):
                chars[start + j] = ch
            else:
                chars.append(ch)
        # If new is shorter than source token, pad with spaces
        old_len = m.end() - m.start()
        if len(new) < old_len:
            for j in range(len(new), old_len):
                chars[start + j] = " "
    return "".join(chars).rstrip()


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
    color: #611;
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
  pre.lyrics {{
    font-family: "Courier New", Courier, monospace;
    font-size: clamp(0.65rem, 2.5vw, 0.95rem);
    line-height: 1.4;
    margin: 0;
    white-space: pre;
    overflow-x: auto;
  }}
  pre.lyrics .chord {{
    color: #b54;
    font-weight: bold;
  }}
</style>
</head>
<body>

<h1>{title}</h1>
<div class="key">Key of {key}</div>

{sections}

</body>
</html>
"""


def esc(s):
    return htmllib.escape(s) if s else ""


def render_section(section, key):
    label = section.get("label", section["type"].title())
    line_blocks = []
    for chord_row, lyric_row in section["lines"]:
        chord_html = esc(transpose_chord_row(chord_row, key))
        if lyric_row:
            line_blocks.append(
                f'<span class="chord">{chord_html}</span>\n{esc(lyric_row)}'
            )
        else:
            line_blocks.append(f'<span class="chord">{chord_html}</span>')
    body = "\n".join(line_blocks)
    return f'<h2>{esc(label)}</h2>\n<pre class="lyrics">\n{body}\n</pre>\n'


def render_song(song, key):
    sections_html = "\n".join(render_section(s, key) for s in song["sections"])
    return HTML_TEMPLATE.format(
        title=esc(song["title"]),
        key=esc(key),
        sections=sections_html,
    )


def load_song(path):
    spec = importlib.util.spec_from_file_location("song_module", path)
    if spec is None or spec.loader is None:
        sys.exit(f"Could not load: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "SONG"):
        sys.exit(f"{path} does not define a SONG dict")
    return mod.SONG


def main():
    parser = argparse.ArgumentParser(
        description="Render a Nashville-notation song file to HTML in any key."
    )
    parser.add_argument("song", help="path to a song .py file (defines SONG dict)")
    parser.add_argument("key", help="target key, e.g. C, G, Eb, F#")
    parser.add_argument(
        "-o", "--output", help="output HTML file (default: stdout)"
    )
    args = parser.parse_args()

    if args.key not in KEY_TO_SEMITONE:
        sys.exit(
            f"Unknown key: {args.key}\n"
            f"Valid keys: {', '.join(sorted(KEY_TO_SEMITONE))}"
        )

    song = load_song(args.song)
    out = render_song(song, args.key)

    if args.output:
        Path(args.output).write_text(out)
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(out)


if __name__ == "__main__":
    main()
