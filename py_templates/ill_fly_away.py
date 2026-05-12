"""
song_template.py — Template for a song data file.
"""

SONG = {
    "title": "I'll Fly Away",
    "sources": [
        # (display name, URL) — shown in the index page's Source column.
        ("UltimateGuitar", "https://tabs.ultimate-guitar.com/tab/alison-krauss/ill-fly-away-chords-3325778"),
    ],
    "sections": [
        {
            "type": "intro",
            "label": "Intro",
            "lines": [
                # Instrumental — second item is None (no lyric row).
                ("|1    |1 17 |4    |1    |", None),
                ("|1    |1    |1 57 |1    |", None),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 1",
            "lines": [
                ("1                                    17",
                 "Some bright morning when this life is over"),
                ("4        1",
                 "I'll fly away"),
                ("1                                    ",
                 "To that home on God's celestial shore"),
                ("1   57   1",
                 "I'll fly away"),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("1                        17",
                 "I'll fly away, fly away, oh glory"),
                ("4        1                      ",
                 "I'll fly away, (in the morning)"),
                ("1",
                 "When I die, Hallelujah by and by"),
                ("1   57   1",
                 "I'll fly away")
            ],
        },
        {
            "type": "verse",
            "label": "Verse 2",
            "lines": [
                ("1                                  17",
                 "When the shadows of this life have gone"),
                ("4        1",
                 "I'll fly away"),
                ("1                                    ",
                 "Like a bird from these prison walls I'll fly"),
                ("1   57      1",
                 "I'll fly away"),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("1                           17",
                 "I'll fly away, fly away, oh glory"),
                ("4        1                      ",
                 "I'll fly away, (in the morning)"),
                ("1",
                 "When I die, Hallelujah by and by"),
                ("1   57   1",
                 "I'll fly away")
            ],
        },
        {
            "type": "solo",
            "label": "Instrumental",
            "lines": [
                ("|1    |1 17 |4    |1    |", None),
                ("|1    |1    |1 57 |1    |", None),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 3",
            "lines": [
                ("1                              17",
                 "Oh, how glad and happy when we meet"),
                ("4        1",
                 "I'll fly away"),
                ("1                                    ",
                 "No more cold iron shackles on my feet"),
                ("1   57      1",
                 "I'll fly away"),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("1                           17",
                 "I'll fly away, fly away, oh glory"),
                ("4        1                      ",
                 "I'll fly away, (in the morning)"),
                ("1",
                 "When I die, Hallelujah by and by"),
                ("1   57   1",
                 "I'll fly away")
            ],
        },
        {
            "type": "solo",
            "label": "Instrumental",
            "lines": [
                ("|1    |1 17 |4    |1    |", None),
                ("|1    |1    |1 57 |1    |", None),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("1                        17",
                 "I'll fly away, fly away, oh glory"),
                ("4        1                      ",
                 "I'll fly away, (in the morning)"),
                ("1",
                 "When I die, Hallelujah by and by"),
                ("1   57   1",
                 "I'll fly away")
            ],
        },
        {
            "type": "verse",
            "label": "Verse 4",
            "lines": [
                ("1                              17",
                 "Just a few more weary days and then"),
                ("4        1",
                 "I'll fly away"),
                ("1                                    ",
                 "To a land where joys will never end"),
                ("1   57      1",
                 "I'll fly away"),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("1                           17",
                 "I'll fly away, fly away, oh glory"),
                ("4        1                      ",
                 "I'll fly away, (in the morning)"),
                ("1",
                 "When I die, Hallelujah by and by"),
                ("1   57   1",
                 "I'll fly away"),
                ("1   57   1",
                 "I'll fly away")
            ],
        },
    ],
}
