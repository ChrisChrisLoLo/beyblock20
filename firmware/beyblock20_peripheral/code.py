import board
import keypad
from i2ctarget import I2CTarget

target = I2CTarget(board.SCL, board.SDA, [0x41])

key_matrix = keypad.KeyMatrix(
    column_pins=(board.D6,board.D3,board.D2,board.D1,board.D0),
    row_pins=(board.D10,board.D9,board.D8,board.D7)
)

import time

while True:
    arr = []
    while True:
        event = key_matrix.events.get()
        if event:
            print("got event")
            arr.append(event.key_number)
            arr.append(int(event.pressed))
        else:
            break
    print("writing byteArr")
    byteArr = bytearray([len(arr)]+arr)
    print(byteArr)
    time.sleep(2)

while True:
    request = target.request()
    if request is not None:
        if not request.is_read:

            r = request.read()
            if r == "T":
                print("Read a T")

            # Schema of the buffer is a series of 2 byte pairs
            # 1 byte representing key position
            # 1 byte representing 1 or 0. This could be optimized to be 1 bit
            
            byteArr = bytearray(64 * 2)
            currInd = 0
            while True:
                event = key_matrix.events.get()
                if event:
                    print("got event")
                    byteArr[currInd] = bytes(event.key_number)[0]
                    byteArr[currInd+1] = bytes(int(event.pressed))[0]
                    currInd += 2
                else:
                    break
            print("writing byteArr")
            print(byteArr)
            request.write(byteArr)

