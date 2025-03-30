def on_button_pressed_a():
    for index in range(1):
        music.ring_tone(659)
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index2 in range(10):
        basic.show_icon(IconNames.NO)
        music.play(music.tone_playable(988, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
