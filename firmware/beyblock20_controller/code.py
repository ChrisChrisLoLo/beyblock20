print("Starting")

import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner

keyboard = KMKKeyboard()

keyboard.keymap = [
    [
        KC.A,KC.B,KC.C,KC.D,KC.E,
        KC.F,KC.G,KC.H,KC.I,KC.J,
        KC.K,KC.L,KC.M,KC.N,KC.O,
        KC.P,KC.Q,KC.R,KC.S,KC.T,

        # KC.A,KC.B,KC.C,KC.D,KC.E,
        # KC.F,KC.G,KC.H,KC.I,KC.J,
        # KC.K,KC.L,KC.M,KC.N,KC.O,
        # KC.P,KC.Q,KC.R,KC.S,KC.T
    ],
]

if __name__ == '__main__':
    keyboard.go()
