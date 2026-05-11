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

  "type"  : semantic type — "verse", "chorus", "bridge", "intro", "outro", "solo", etc.
            (Used as the default label if no explicit one is given.)
  "label" : (optional) the header shown above the section, e.g. "Verse 1",
            "Chorus 1", "Verse Solo Break". If omitted, falls back to type.title().
  "lines" : list of (chord_row, lyric_row) tuples.
            For instrumental lines (e.g. solo breaks), set lyric_row to None.
"""

SONG = {
    "title": "Ragged But Right",
    "sections": [
        {
            "type": "verse",
            "label": "Verse 1",
            "lines": [
                ("1                                   5",
                 "I come here to tell you that I'm ragged but right"),
                ("5                                1",
                 "I'm a thief and a gambler, I get drunk every night"),
                ("      4                               1          6 ",
                 "Eat a porterhouse steak three times a day for my board"),
                ("       2                           5",
                "That's more than any loafer in this town can afford"),
                ("1                             5",
                 "A big electric fan to keep me cool while I sleep"),
                ("  5                       1",
                 "A little baby girl dancin round at my feet"),
                ("       4                          1           6",
                 "I am a ramblin' gambler and I get drunk every night"),
                ("2                 5          1",
                 "Boys you know I'm ragged but right")
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus 1",
            "lines": [
                ("1",
                 "I go everywhere, I don't pay no fare"),
                ("             2             5  1",
                 "I can ride a freight train anywhere"),
                ("1                4              ",
                 "If I win or lose, I don't get no blues"),
                ("        1              5           1",
                 "Oh it's a-ramblin' and rollin' for me")
            ],
        },
        {
            "type": "solo",
            "label": "Verse Solo Break",
            "lines": [
                # Instrumental — second item is None (no lyric row).
                ("|1    |5    |5    |1    |", None),
                ("|4 1  |1 6m |2    |5    |", None)
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus 2",
            "lines": [
                ("1                           5",
                 "Well I never got married, I never settled down"),
                ("                                   1",
                 "Never spent more than one night in any one town"),
                ("4                         1             6",
                 "I've got no family and no place to call home"),
                ("2                      5",
                 "But I'll stay happy as long as I roam")
            ],
        },
        {
            "type": "verse",
            "label": "Verse 2",
            "lines": [
                ("1                              5",
                 "I hopped on a freight train in North Caroline"),
                ("5                        1",
                 "Rode down to Atlanta and bought me some shine"),
                ("4                          1       6 ",
                 "Went into a card game with 39 cents"),
                ("2                       5",
                "Came out with enough for another month's rent"),
                ("1                                   5",
                 "Well you may think I'm bragging but don't get me wrong"),
                ("  5                               1",
                 "I can't run for office while I'm singing this song"),
                ("       4                          1           6",
                 "I'm a thief and a gambler and I'm drunk every night"),
                ("2                 5          1",
                 "I tell you boys I'm ragged but right.")
            ],
        },
        {
            "type": "outro",
            "label": "Outro",
            "lines": [
                ("  27                 57",
                 "I tell you boys I'm ragged"),
                ("  27                  57",
                 "I tell you boys I'm ragged"),
                ("  27                 57         1",
                 "I tell you boys I'm ragged but right.")
            ],
        },
    ],
}
