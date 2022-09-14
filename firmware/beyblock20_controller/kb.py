import board
import busio

from i2c_scanner import I2CScanner
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner

class KMKKeyboard(_KMKKeyboard):

    col_pins = (board.D6,board.D3,board.D2,board.D1,board.D0)
    row_pins = (board.D10,board.D9,board.D8,board.D7)
    diode_orientation = DiodeOrientation.COL2ROW

    i2c = busio.I2C(board.D5, board.D4)

    matrix = [
        MatrixScanner(
            # required arguments:
            column_pins=col_pins,
            row_pins=row_pins,
            # optional arguments with defaults:
            columns_to_anodes=DiodeOrientation.COL2ROW,
            interval=0.02,
            max_events=64
        ),  
        I2CScanner(
            # beyblock20 peripheral
            key_count=4*5,
            i2c=i2c,
            i2c_address=0x41
        ),
        I2CScanner(
            # knoblin3 peripheral
            key_count=2*3,
            i2c=i2c,
            i2c_address=0x51
        )
    ]