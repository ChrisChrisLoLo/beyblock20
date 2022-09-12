import board
from i2ctarget import I2CTarget

target = I2CTarget(board.SCL, board.SDA, [0x41])

while True:
    request = target.request()
    if request is not None:
        if request.is_read:
            print("Write request ")
            request.write(b'B')
        else:
            r = request.read()
            if r == "T":
                print("Read a T")