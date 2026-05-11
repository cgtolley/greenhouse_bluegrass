"""
song_template.py — Template for a song data file.
"""

SONG = {
    "title": "Big Rock Candy Mountain",
    "sections": [
        {
            "type": "intro",
            "label": "Intro",
            "lines": [
                ("    1                                           5        1",
                 "One evening as the sun went down and the jungle fire was burning"),
                ("         1                                            5       1",
                 "Down the track came a hobo hiking and he said, 'Boys, I'm not turning'"),
                ("    4            1           4    1     4         1       5",
                 "I'm headed for a land that's far away besides the crystal fountains"),
                ("   1                                  5              1",
                 "So come with me, we'll go and see the Big Rock Candy Mountains"),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 1",
            "lines": [
                ("    1                                     4                    1",
                 "In the Big Rock Candy Mountains there's a land that's fair and bright,"),
                ("         4                 1               4              5",
                 "where the handouts grow on bushes and you sleep out every night"),
                ("          1                             4                1",
                "Where the boxcars all are empty and the sun shines every day"),
                ("       4             1            4         1          4        ",
                 "on the birds and the bees and the cigarette trees, the lemonade "),
                ("1                 4        1            5              1",
                 "springs where the bluebird sings in the Big Rock Candy Mountains"),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 2",
            "lines": [
                ("       1                                4                1",
                 "In the Big Rock Candy Mountains all the cops have wooden legs,"),
                ("        4                 1                    4                    5",
                 "and the bulldogs all have rubber teeth and the hens lay soft-boiled eggs"),
                ("   1                                        4                1",
                "The farmers' trees are full of fruit and the barns are full of hay"),
                ("       4         1              4        1               4          ",
                 "Oh, I'm bound to go where there ain't no snow, where the rain"), 
                ("      1         4          1           5              1",
                 "don't fall, the wind don't blow in the Big Rock Candy Mountains"),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 3",
            "lines": [
                ("       1                            4                 1",
                 "In the Big Rock Candy Mountains you never change your socks,"),
                ("        4                 1              4                  5",
                 "and the little streams of alcohol come a trickling down the rocks"),
                ("   1                                       4                  1",
                "The brakemen have to tip their hats and the railroad bulls are blind"),
                ("          4       1           4       1            4           1       ",
                 "There's a lake of stew and of whiskey too, you can paddle all around"),
                ("4      1         5              1",
                 "'em in a big canoe in the Big Rock Candy Mountains"),
            ],
        },
        {
            "type": "verse",
            "label": "Verse 4",
            "lines": [
                ("       1                            4                 1",
                 "In the Big Rock Candy Mountains the jails are made of tin"),
                ("    4                  1            4               5",
                 "and you can walk right out again as soon as you are in"),
                ("     1                                  4             1",
                "There ain't no short-handled shovels, no axes, saws or picks"),
                ("      4     1              4         1               4        1",
                 "I'm a gonna stay where you sleep all day, where they hung the Turk"),
                ("     4        1           5              1",
                 "that invented work in the Big Rock Candy Mountains"),
            ],
        },
        {
            "type": "solo",
            "label": "Instrumental",
            "lines": [
                # Instrumental — second item is None (no lyric row).
                ("|1    |4 1  |4 1  |4 1  |", None),
            ],
        },
        {
            "type": "outro",
            "label": "Outro",
            "lines": [
                ("     4       1        4      1           5              4",
                 "I'll see you all this comin' fall in the Big Rock Candy Mountains"),
            ],
        },
    ],
}
