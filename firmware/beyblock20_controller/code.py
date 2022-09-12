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
    #keyboard.go()
    # try to run i2c example

    import board
    import time


    import busio
    # i2c = board.I2C()

    i2c = busio.I2C(board.D5, board.D4)

    while True:
        i2c.try_lock()

        print(
            "I2C addresses found:",
            [hex(device_address) for device_address in i2c.scan()],
        )

        print("Sending T")
        i2c.writeto(0x41, b'T')
        time.sleep(1)


        # up to 64 events * 2 bytes
        t_bytes = bytearray((64 * 2)+1)
        i2c.readfrom_into(0x41, t_bytes)
        print("Read ", t_bytes)
        i2c.unlock()
        time.sleep(5)