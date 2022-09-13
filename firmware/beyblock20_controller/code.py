print("Starting")

from kb import KMKKeyboard
from kmk.keys import KC
# from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData

keyboard = KMKKeyboard()

# oled_ext = Oled(
#     OledData(
#         corner_one={0:OledReactionType.STATIC,1:["layer"]},
#         corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
#         corner_three={0:OledReactionType.LAYER,1:["base","raise","lower","adjust"]},
#         corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","shifted","leds"]}
#     ),
#     toDisplay=OledDisplayMode.TXT,
#     flip=False
#     )

# keyboard.extensions.append(oled_ext) 

keyboard.keymap = [
    [
        KC.A,KC.B,KC.C,KC.D,KC.E,
        KC.F,KC.G,KC.H,KC.I,KC.J,
        KC.K,KC.L,KC.M,KC.N,KC.O,
        KC.P,KC.Q,KC.R,KC.S,KC.T,

        KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,
        KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,
        KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,
        KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,
    ],
]

if __name__ == '__main__':
    keyboard.go()