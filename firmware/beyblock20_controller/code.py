print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D6,board.D3,board.D2,board.D1,board.D0)
keyboard.row_pins = (board.D10,board.D9,board.D8,board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.A,KC.B,KC.C,KC.D,KC.E,
        KC.F,KC.G,KC.H,KC.I,KC.J,
        KC.K,KC.L,KC.M,KC.N,KC.O,
        KC.P,KC.Q,KC.R,KC.S,KC.T
    ],
]

if __name__ == '__main__':
    keyboard.go()
