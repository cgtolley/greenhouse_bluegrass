"""
song_template.py — Template for a song data file.

Format
------
SONG is a dict with two keys:
  "title"   : the song title (string)
  "sections": a list of section dicts
"""

SONG = {
    "title": "Way Over Yonder In the Minor Key",
    "sources": [
        # (display name, URL) — shown in the index page's Source column.
        ("UltimateGuitar", "https://tabs.ultimate-guitar.com/tab/billy-bragg/way-over-yonder-in-the-minor-key-chords-970744"),
    ],
    "sections": [
        {
            "type": "verse",
            "label": "Verse 1",
            "lines": [
                ("1                         4",
                 "I lived in a place called Okfuskee"),
                ("4                                   1",
                 "And I had a little girl in a holler tree"),
                ("4                                  1  ",
                 "I said, little girl, it's plain to see"),
                ("5                               1",
                 "Ain't nobody that can sing like me"),
                ("5                               6",
                 "Ain't nobody that can sing like me"),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 2",
            "lines": [
                ("1                         4",
                 "She said it's hard for me to see"),
                ("4                                   1",
                 "And I had a little girl in a holler tree"),
                ("4                                  1  ",
                 "I said, little girl, it's plain to see"),
                ("5                               1",
                 "Ain't nobody that can sing like me"),
                ("5                               6",
                 "Ain't nobody that can sing like me"),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("4                            1",
                 "Way over yonder in the minor key"),
                ("6                            1",
                 "Way over yonder in the minor key"),
                ("5                                     6",
                 "There ain't nobody that can sing like me "),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 3",
            "lines": [
                ("1                         4",
                 "Her mama cut a switch from a cherry tree"),
                ("4                                   1",
                 "And laid it for she and me"),
                ("4                                  1  ",
                 "It stung lots worse than a hive of bees"),
                ("          5                               1",
                 "But there ain't nobody that can sing like me"),
                ("5                               6",
                 "Ain't nobody that can sing like me"),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 4",
            "lines": [
                ("1                             4",
                 "Now I have walked a long long ways"),
                ("4                                      1",
                 "And I still look back to my Tanglewood days"),
                ("4                                    1  ",
                 "I've led lots of girls since then to stray"),
                ("       5                               1",
                 "Sayin' ain't nobody that can sing like me"),
                ("5                               6",
                 "Ain't nobody that can sing like me"),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("4                            1",
                 "Way over yonder in the minor key"),
                ("6                            1",
                 "Way over yonder in the minor key"),
                ("5                                     6",
                 "There ain't nobody that can sing like me "),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("4                            1",
                 "Way over yonder in the minor key"),
                ("6                            1",
                 "Way over yonder in the minor key"),
                ("5                                     6",
                 "There ain't nobody that can sing like me "),
                ("5                                     6",
                 "There ain't nobody that can sing like me "),
            ],
        },
        {
            "type": "solo",
            "label": "Instrumental x2",
            "lines": [
                ("|1    |1  17|4    |1    |", None),
                ("|1    |1    |5    |1    |", None),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 2",
            "lines": [
                ("1                              17",
                 "Oh, how glad and happy when we meet"),
                ("4        1",
                 "I'll fly away"),
                ("1                               ",
                 "No more cold iron shackles on my feet"),
                ("    5   1",
                 "I'll fly away"),
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
