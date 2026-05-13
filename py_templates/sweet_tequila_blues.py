"""
song_template.py — Template for a song data file.

Format
------
SONG is a dict with two keys:
  "title"   : the song title (string)
  "sections": a list of section dicts
"""

SONG = {
    "title": "Sweet Tequila Blues by Chip Taylor and Carrie Rodriguez",
    "sources": [
        # (display name, URL) — shown in the index page's Source column.
        ("cowboylyrics", "https://www.cowboylyrics.com/tabs/chip-taylor-and-carrie-rodriguez/sweet-tequila-blues-19872.html"),
    ],
    "sections": [
        {
            "type": "intro",
            "label": "Intro",
            "lines": [
                ("|1    |1    |3m/7 |4/1  |", None),
                ("|1    |5/2  |1    |1    |", None),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("    1                       4            1",
                 "And I keep lookin for it, I hope I never find it"),
                ("                                            5",
                 "If I get close to it, just put me on a train"),
                ("   1                         3                4   ",
                 "An get me back to Austin, oh damn I miss that town"),
                ("           1             5            1",
                 "I got them sweet tequila blues comin' down"),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 1",
            "lines": [
                ("6m       1         4                1",
                 "I knew a man, with money in his hand"),
                ("     6m                1               5",
                 "He'd look that Jack of Diamonds in the eye"),
                ("     6m               1           4              1     ",
                 "He'd place it on the four and let seven close the door"),
                ("                              5                  1",
                 "He'd take all them chips and lay right down and cry"),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("    1                       4            1",
                 "And I keep lookin for it, I hope I never find it"),
                ("                                            5",
                 "If I get close to it, just put me on a train"),
                ("   1                         3                4   ",
                 "An get me back to Austin, oh damn I miss that town"),
                ("           1             5            1",
                 "I got them sweet tequila blues comin' down"),
            ],
        },
        {
            "type": "solo",
            "label": "Instrumental",
            "lines": [
                ("|1    |1    |4    |1    |", None),
                ("|1    |1    |5    |5    |", None),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 2",
            "lines": [
                ("6m       1         4                     1",
                 "I knew a girl who thought she had the world"),
                ("      6m               1            5",
                 "With a slightly racin' spanish lullaby"),
                ("        6m               1                  4                1     ",
                 "WHen her dream came into town she threw the whole damn thing around"),
                ("                      5               1",
                 "Some texas girls just love to say goodbye"),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("    1                       4            1",
                 "And I keep lookin for it, I hope I never find it"),
                ("                                            5",
                 "If I get close to it, just put me on a train"),
                ("   1                         3                4   ",
                 "An get me back to Austin, oh damn I miss that town"),
                ("           1             5            1",
                 "I got them sweet tequila blues comin' down"),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 2",
            "lines": [
                ("       6m          1            4              1",
                 "Here's one for the ladies, baby where is my Mercedes?"),
                ("         6m               1              5",
                 "Girl I'm waiting for the ribbons and the bows"),
                ("6m           1           4           1     ",
                 "Just keep me guessin, oh baby I'm confessin'"),
                ("                       5                 1",
                 "I know you want two of them and three of those"),
            ],
        },
        {
            "type": "chorus",
            "label": "Chorus",
            "lines": [
                ("    1                       4            1",
                 "And I keep lookin for it, I hope I never find it"),
                ("                                            5",
                 "If I get close to it, just put me on a train"),
                ("   1                         3                4   ",
                 "An get me back to Austin, oh damn I miss that town"),
                ("           1             5            1",
                 "I got them sweet tequila blues comin' down"),
            ],
        },
        {
            "type": "solo",
            "label": "Instrumental",
            "lines": [
                ("|1    |1    |4    |1    |", None),
                ("|1    |1    |5    |5    |", None),
            ],
        },
        {
            "type": "outro",
            "label": "Outro",
            "lines": [
                ("   1                         3                4   ",
                 "An get me back to Austin, oh damn I miss that town"),
                ("           1             5            1",
                 "I got them sweet tequila blues comin' down"),
                ("           1             5            1",
                 "I got them sweet tequila blues comin' down"),
            ],
        },
    ],
}
