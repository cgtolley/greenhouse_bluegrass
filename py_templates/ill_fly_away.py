"""
song_template.py — Template for a song data file.

Copy this file, rename it (e.g. ragged_but_right.py), and fill in your song.
Then render with:

    python render_song.py YOUR_SONG.py KEY -o output.html

Format
------
SONG is a dict with two keys:
  "title"   : the song title (string)
  "sections": a list of section dicts

Each section dict has:
  "type"  : semantic type — "verse", "chorus", "bridge", "intro", "outro", "solo", etc.
            (Used as the default label if no explicit one is given.)
  "label" : (optional) the header shown above the section, e.g. "Verse 1",
            "Chorus 1", "Verse Solo Break". If omitted, falls back to type.title().
  "lines" : list of (chord_row, lyric_row) tuples.
            For instrumental lines (e.g. solo breaks), set lyric_row to None.

Chord notation (Nashville)
--------------------------
  1, 4, 5         major triads
  2m, 3m, 6m      minor triads
  57, 17          dominant 7ths
  1maj7           major 7th
  5/7             slash chord (5 over its 7th degree as bass)
  1sus4, 5sus     suspended
  b3, #4          chromatic alterations

Alignment
---------
Each chord in chord_row is placed at the same character column when rendered.
Use spaces to position each chord above the lyric syllable where it changes.
The "counts" comments below are just for your own reference — they're ignored
by the renderer.

Gotcha: if a chord transposes to a longer name (e.g. `4` → `Bb` in F is 2 chars),
it overwrites the following space. Leave a few characters of breathing room
between chord symbols in the source.
"""

SONG = {
    "title": "Song Title Here",
    "sources": [
        # (display name, URL) — shown in the index page's Source column.
        ("ExampleSite", "https://example.com/some-song-page"),
    ],
    "sections": [
        {
            "type": "verse",
            "label": "Verse 1",
            "lines": [
                # counts: 1   2   3   4   5   6   7   8
                # cols:   0   6   12  18  24  30  36  42
                ("1                                   5",
                 "Placeholder lyric line one goes right here"),
                ("5                                1",
                 "Placeholder lyric line two goes right here"),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus 1",
            "lines": [
                ("1",
                 "Placeholder chorus line one goes here"),
                ("                                  5  1",
                 "Placeholder chorus line two goes here"),
            ],
        },
        {
            "type": "solo",
            "label": "Verse Solo Break",
            "lines": [
                # Instrumental — second item is None (no lyric row).
                ("|1    |5    |5    |1    |", None),
                ("|4 1  |1 6m |2    |5    |", None),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 2",
            "lines": [
                ("1                              5",
                 "Placeholder lyric line goes here"),
            ],
        },
        {
            "type": "outro",
            "label": "Outro",
            "lines": [
                ("  57                 17",
                 "Placeholder outro line one"),
                ("  5                  1",
                 "Placeholder outro line two"),
            ],
        },
    ],
}
