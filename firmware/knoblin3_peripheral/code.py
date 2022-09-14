import board
from rot_encoder import RotaryioEncoder

from i2ctarget import I2CTarget

encoders = [
    RotaryioEncoder(board.D10,board.D9,0),
    RotaryioEncoder(board.D8,board.D7,2),
    RotaryioEncoder(board.D0,board.D1,4),
]

# TODO: Only one encoder can be turned at a time

with I2CTarget(board.D5, board.D4, [0x51]) as device:
    print("Starting peripheral")
    while True:
        request = device.request()
        if not request:
            continue
        with request: 
            if request.is_read:
                not_null = 0
                key_number = 0
                pressed = 0
                
                for encoder in encoders:
                    event = encoder.scan_for_changes()
                    if event:
                        not_null = 1
                        key_number = event.key_number
                        pressed = event.pressed
                        break                    
                        
                byteArr = bytearray([not_null,key_number,pressed])
                print(byteArr)
                request.write(byteArr)
            else:
                r = request.read()
                # regardless of request, process key matrix
                if r == "T":
                    print("Read a T")