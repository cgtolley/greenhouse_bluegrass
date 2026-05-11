"""
song_template.py — Template for a song data file.
"""

SONG = {
    "title": "Song Title Here",
    "sections": [
        {
            "type": "verse",
            "label": "Verse 1",
            "lines": [
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
