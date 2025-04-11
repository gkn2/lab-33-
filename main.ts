music.setVolume(255)
music.playMelody("C D E F G A B", 140)
music.playMelody("C D E F G A B:8", 140)
music.playMelody("C C# D D# E F F# G G# A A# B", 140)
let melody = ["E D C D", "E E E:8", "D D D:8", "E G G:8", "E D C D", "E E E E", "D D E D C:8"]
for (let measure of melody) {
    music.playMelody(measure, 80)
}
let jaws_theme = ["E2 R", "E2 R", "E2 R", "E2 R", "E2 E2 R", "E2 E2 R", "E2 E2 E2:8"]
for (let part of jaws_theme) {
    music.playMelody(part, 70)
}
