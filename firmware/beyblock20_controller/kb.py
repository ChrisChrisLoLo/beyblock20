import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner


class KMKKeyboard(_KMKKeyboard):

    col_pins = (board.D6,board.D3,board.D2,board.D1,board.D0)
    row_pins = (board.D10,board.D9,board.D8,board.D7)
    diode_orientation = DiodeOrientation.COL2ROW

    matrix = [MatrixScanner(
        # required arguments:
        column_pins=col_pins,
        row_pins=row_pins,
        # optional arguments with defaults:
        columns_to_anodes=DiodeOrientation.COL2ROW,
        interval=0.02,
        max_events=64
    )]