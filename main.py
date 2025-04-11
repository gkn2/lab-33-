music.set_volume(255)




music.play_melody("C D E F G A B", 140)




music.play_melody("C D E F G A B:8", 140)




music.play_melody("C C# D D# E F F# G G# A A# B", 140)




melody = [
    "E D C D",
    "E E E:8",
    "D D D:8",
    "E G G:8",
    "E D C D",
    "E E E E",
    "D D E D C:8"
]



for measure in melody:
    music.play_melody(measure, 80)




jaws_theme = [
    "E2 R",
    "E2 R",
    "E2 R",
    "E2 R",
    "E2 E2 R",
    "E2 E2 R",
    "E2 E2 E2:8"
]



for part in jaws_theme:
    music.play_melody(part, 70)