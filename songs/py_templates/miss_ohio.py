"""
song_template.py — Template for a song data file.

Copy this file, rename it (e.g. ragged_but_right.py), and fill in your song.
Then render with:

    python render_song.py YOUR_SONG.py KEY -o output.html

SONG = {
    "title": "Look at Miss Ohio",
    "sections": [
        {
            "type": "intro",
            "label": "Intro",
            "lines": [
                ("| 1 | 5 | 2 | 3m 2 |", None),
                ("| 1 | 5 | 1 |, None)
        }
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("1        5      2            3m 2",
                 "Oh me oh my oh, look at Miss O-hio"),
                ("        1                       5       2",
                 "She's a-running around with her rag-top down"),
                 ("           1                  5         2",
                 "She says I wanna do right but not right now")
            ],
        },
        {
            "type": "verse",
            "label": "Verse 1",
            "lines": [
                ("      1           5        2             3m  2",
                 "Gonna drive to Atlanta and live out this fantasy"),
                ("1                      5       2",
                 "Running around with the rag-top down"),
                 ("       1                  5            2",
                 "Yeah I wanna do right but not right now")
            ],
        },
        {
            "type": "solo",
            "label": "Instrumental",
            "lines": [
                # Instrumental — second item is None (no lyric row).
                ("| 3m | 67 |", None),
                ("| 3m | 67 |", None),
                ("| 1 | 5 | 2 | 3m 2 |", None),
                ("| 1 | 5 | 2 |", None),
            ],
        },
    ],
}
