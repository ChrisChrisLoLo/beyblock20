from keypad_python_impl import EventQueue

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
        row_count,
        col_count,
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
        # self._row_digitalinouts = []
        # for row_pin in row_pins:
        #     row_dio = digitalio.DigitalInOut(row_pin)
        #     row_dio.switch_to_input(
        #         pull=(digitalio.Pull.UP if columns_to_anodes else digitalio.Pull.DOWN)
        #     )
        #     self._row_digitalinouts.append(row_dio)

        # self._column_digitalinouts = []
        # for column_pin in column_pins:
        #     col_dio = digitalio.DigitalInOut(column_pin)
        #     col_dio.switch_to_input(
        #         pull=(digitalio.Pull.UP if columns_to_anodes else digitalio.Pull.DOWN)
        #     )
        #     self._column_digitalinouts.append(col_dio)
        self.row_count = row_count
        self.col_count = col_count
        self._currently_pressed = [False] * col_count * row_count
        self._previously_pressed = [False] * col_count * row_count
        self._events = EventQueue(max_events)
        
        self.i2c = i2c
        self.i2c_address = i2c_address



        # super().__init__(interval, max_events, self._keypad_keymatrix_scan)

    # pylint: enable=too-many-arguments

    @property
    def key_count(self):
        """The number of keys that are being scanned. (read-only)"""
        return self.row_count * self.col_count

    def scan_for_changes(self):

        # Return event if already in the backlog
        backlog_event = self._events.get()
        if backlog_event:
            return backlog_event
            

        self.i2c.try_lock()
        # print(
        #     "I2C addresses found:",
        #     [hex(device_address) for device_address in self.i2c.scan()],
        # )

        # print("Sending T")
        # i2c.writeto(0x41, b'T')
        # i2c.writeto(0x3c, b'T')

        # self.i2c.writeto(self.i2c_address, b'T')

        # up to 64 events * 2 bytes
        received_bytes = bytearray(3)
        self.i2c.readfrom_into(self.i2c_address, received_bytes)
        self.i2c.unlock()

        # checks if event
        event_not_null = int(received_bytes[0])

        if event_not_null:
            print("Read ", received_bytes)
            return KeyEvent(
                key_number=int(received_bytes[1])+self.offset,
                pressed=int(received_bytes[2])
            )
            #self._events.keypad_eventqueue_record(int(received_bytes[1]), int(received_bytes[2]))


        # return 1st event from scan, even if it's None
        # return self._events.get()

# class I2CMatrix():
#     """
#     Implements a keypad interface that makes I2C requests to peripherals.

#     """
#     # pylint: disable=too-many-arguments


#     def deinit(self):
#         """Stop scanning and release the pins."""
#         super().deinit()

#     def reset(self):
#         """
#         Reset the internal state of the scanner to assume that all keys are now released.
#         Any key that is already pressed at the time of this call will therefore immediately cause
#         a new key-pressed event to occur.
#         """
#         self._previously_pressed = self._currently_pressed = [False] * self.key_count

#     def _row_column_to_key_number(self, row, column):
#         return (row * self.col_count) + column

    

