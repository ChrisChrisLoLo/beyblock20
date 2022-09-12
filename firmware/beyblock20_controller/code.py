print("Starting")

import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner

class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [MatrixScanner(
            # required arguments:
            column_pins=self.col_pins,
            row_pins=self.row_pins,
            # optional arguments with defaults:
            columns_to_anodes=DiodeOrientation.COL2ROW,
            interval=0.02,
            max_events=64
        )]
        super().__init__()

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
