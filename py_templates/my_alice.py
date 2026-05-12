"""
song_template.py — Template for a song data file.
"""

SONG = {
    "title": "My Alice by Billy Strings",
    "sources": [
        # (display name, URL) — shown in the index page's Source column.
        ("UltimateGuitar", "https://tabs.ultimate-guitar.com/tab/billy-strings/my-alice-chords-4425650e"),
    ],
    "sections": [
         {
            "type": "intro",
            "label": "Intro",
            "lines": [
                # Instrumental — second item is None (no lyric row).
                ("|1m   |7b 5m|7b   |1m    |", None),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 1",
            "lines": [
                ("1m                 7b               5m",
                 "Early in the fall, back deep in the woods"),
                ("7b                              1m ",
                 "The first hint of frost is upon you"),
            ],
        },
        
    ],
}
