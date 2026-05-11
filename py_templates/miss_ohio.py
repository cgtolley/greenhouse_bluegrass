"""
song_template.py — Template for a song data file.

Copy this file, rename it (e.g. ragged_but_right.py), and fill in your song.
Then render with:

    python render_song.py YOUR_SONG.py KEY -o output.html
"""
SONG = {
    "title": "Look at Miss Ohio",
    "sources": [
        ("UltimateGuitar", "https://tabs.ultimate-guitar.com/tab/gillian-welch/look-at-miss-ohio-chords-1089277"),
        ],
    "sections": [
        {
            "type": "intro",
            "label": "Intro",
            "lines": [
                ("| 4 | 1 | 5 | 6m 5 |", None),
                ("| 4 | 1 | 4 |", None)
                ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("4        1      5            6m 5",
                 "Oh me oh my oh, look at Miss O-hio"),
                ("        4                       1       5",
                 "She's a-running around with her rag-top down"),
                 ("           4                  1         5",
                 "She says I wanna do right but not right now")
            ],
        },
        {
            "type": "verse",
            "label": "Verse 1",
            "lines": [
                ("      4           1        5             6m  5",
                 "Gonna drive to Atlanta and live out this fantasy"),
                ("4                      1       5",
                 "Running around with the rag-top down"),
                 ("       4                  1          5",
                 "Yeah I wanna do right but not right now")
            ],
        },
        {
            "type": "solo",
            "label": "Instrumental",
            "lines": [
                ("| 6m | 27 |", None),
                ("| 6m | 27 |", None),
                ("| 4 | 1 | 5 | 6m 5 |", None),
                ("| 4 | 1 | 5 |", None),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 2",
            "lines": [
                ("         4           1        5                6m  5",
                 "Had your arm around her shoulder, a regimental soldier"),
                ("    4                         1       5",
                 "An' mamma starts pushing that wedding gown"),
                 ("        4                  1         5",
                 "Yeah you wanna do right but not right now")
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("4        1      5            6m 5",
                 "Oh me oh my oh, look at Miss O-hio"),
                ("        4                       1       5",
                 "She's a-running around with her rag-top down"),
                 ("           4                  1         5",
                 "She says I wanna do right but not right now")
            ],
        },
        {
            "type": "solo",
            "label": "Instrumental",
            "lines": [
                ("| 6m | 27 |", None),
                ("| 6m | 27 |", None),
                ("| 4 | 1 | 5 | 6m 5 |", None),
                ("| 4 | 1 | 5 |", None),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 2",
            "lines": [
                ("  4           1        5                  6m  5",
                 "I know all about it, so you don't have to shout it"),
                ("    4                   1       5",
                 "I'm gonna straighten it out somehow"),
                 ("        4                  1         5",
                 "Yeah I wanna do right but not right now")
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("4        1      5            6m 5",
                 "Oh me oh my oh, look at Miss O-hio"),
                ("        4                       1       5",
                 "She's a-running around with her rag-top down"),
                 ("           4                  1         5",
                 "She says I wanna do right but not right now"),
                 ("     4                  1         5",
                  "Oh I wanna do right but not right now"),
            ],
        },
        {
            "type": "outro",
            "label": "Outro",
            "lines": [
                ("| 4 | 1 | 5 | 6m 5 |", None),
                ("| 4 | 1 | 5 |", None),
                ("| 4 | 1 | 5 | 6m 5 |", None),
                ("| 4 | 1 | 5 |", None)
                ],
        },
    ],
}
