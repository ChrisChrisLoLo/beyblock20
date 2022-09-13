import board
import keypad
from i2ctarget import I2CTarget

target = I2CTarget(board.SCL, board.SDA, [0x41])

key_matrix = keypad.KeyMatrix(
    column_pins=(board.D6,board.D3,board.D2,board.D1,board.D0),
    row_pins=(board.D10,board.D9,board.D8,board.D7)
)

while True:
    request = target.request()
    if request is not None:
        # Schema of the buffer is a series of 2 byte pairs
        # 1 byte representing key position
        # 1 byte representing 1 or 0. This could be optimized to be 1 bit
        if request.is_read:
            not_null = 0
            key_number = 0
            pressed = 0
            
            event = key_matrix.events.get()
            if event:
                not_null = 1
                key_number = event.key_number
                pressed = event.pressed
                    
            byteArr = bytearray([not_null,key_number,pressed])
            # print(byteArr)
            request.write(byteArr)
        else:
            r = request.read()
            # regardless of request, process key matrix
            if r == "T":
               print("Read a T")
