input.onButtonPressed(Button.A, function on_button_pressed_a() {
    for (let index = 0; index < 1; index++) {
        music.ringTone(659)
        basic.showIcon(IconNames.Yes)
    }
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showLeds(`
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    for (let index2 = 0; index2 < 10; index2++) {
        basic.showIcon(IconNames.No)
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
})
basic.forever(function on_forever() {
    
})
