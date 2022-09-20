from kmk.scanners.keypad import Scanner
from keypad import Event as KeyEvent

class I2CScanner(Scanner):
    '''
    Row/Column matrix using the CircuitPython 7 keypad scanner.

    :param row_pins: A sequence of pins used for rows.
    :param col_pins: A sequence of pins used for columns.
    :param direction: The diode orientation of the matrix.
    '''

    def __init__(
        self,
        key_count,
        i2c,
        i2c_address,
        max_events=64,
    ):
        """
        The keys are numbered sequentially from zero. A key number can be computed
        by ``row * len(column_pins) + column``.

        An `EventQueue` is created when this object is created and is available in the `events`
        attribute.

        :param int row_pins_count: The count of pins attached to the rows.
        :param int column_pins_count: The count of pins attached to the colums.
        :param i2c: i2c object.
        :param hex i2c_address: The address of the peripheral.

        """

        self._key_count = key_count
        self._currently_pressed = [False] * key_count
        self._previously_pressed = [False] * key_count
        
        self.i2c = i2c
        self.i2c_address = i2c_address

        self.has_warned_i2c_not_found = False

        #self._curr_i2c_addrs = []

        # super().__init__(interval, max_events, self._keypad_keymatrix_scan)

    # pylint: enable=too-many-arguments

    @property
    def key_count(self):
        """The number of keys that are being scanned. (read-only)"""
        return self._key_count

    def scan_for_changes(self):

        received_bytes = bytearray(3)

        try:
            # If we cannot lock this time around, let other scanners run in meantime
            # if not self.i2c.try_lock():
            #     return

            self.i2c.try_lock()
            # print(
            #     "I2C addresses found:",
            #     [hex(device_address) for device_address in self.i2c.scan()],
            # )

            # print("Sending T")
            # i2c.writeto(0x41, b'T')
            # i2c.writeto(0x3c, b'T')

            self.i2c.writeto(self.i2c_address, b'T')

            # up to 64 events * 2 bytes
            self.i2c.readfrom_into(self.i2c_address, received_bytes)
            self.i2c.unlock()
            
            # reset warning on success
            if self.has_warned_i2c_not_found:
                self.has_warned_i2c_not_found = False

        except OSError as e:
            if e.errno == 19:
                # No device found, warn once and pass
                if not self.has_warned_i2c_not_found:
                    print("WARNING: I2C Device no longer found!")
                    self.has_warned_i2c_not_found = True
            elif e.errno == 116:
                # bus timeout, ignore and wait for peripheral to restart
                print("WARNING: I2C Connection timed out! Waiting for peripheral to restart...")
            else:
                raise


        # checks if event
        event_not_null = int(received_bytes[0])

        if event_not_null == 1:
            print("Read ", received_bytes)
            return KeyEvent(
                key_number=int(received_bytes[1])+self.offset,
                pressed=int(received_bytes[2])
            )
