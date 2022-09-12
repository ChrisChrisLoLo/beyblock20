import keypad
from keypad import _KeysBase

from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeypadScanner


class MatrixScanner(KeypadScanner):
    '''
    Row/Column matrix using the CircuitPython 7 keypad scanner.

    :param row_pins: A sequence of pins used for rows.
    :param col_pins: A sequence of pins used for columns.
    :param direction: The diode orientation of the matrix.
    '''

    def __init__(
        self,
        row_pins,
        column_pins,
        *,
        columns_to_anodes=DiodeOrientation.COL2ROW,
        interval=0.02,
        max_events=64,
    ):
        self.keypad = keypad.KeyMatrix(
            row_pins,
            column_pins,
            columns_to_anodes=(columns_to_anodes == DiodeOrientation.COL2ROW),
            interval=interval,
            max_events=max_events,
        )
        super().__init__()


class I2CKeyMatrix(_KeysBase):
    """
    Implements a keypad interface that makes I2C requests to peripherals.

    """
    # pylint: disable=too-many-arguments
    def __init__(
        self,
        row_count,
        col_count,
        interval=0.02,
        max_events=64,
    ):
        """
        The keys are numbered sequentially from zero. A key number can be computed
        by ``row * len(column_pins) + column``.

        An `EventQueue` is created when this object is created and is available in the `events`
        attribute.

        :param int row_pins_count: The count of pins attached to the rows.
        :param int column_pins_count: The count of pins attached to the colums.
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
        self._currently_pressed = [False] * len(col_count) * len(row_count)
        self._previously_pressed = [False] * len(col_count) * len(row_count)

        super().__init__(interval, max_events, self._keypad_keymatrix_scan)

    # pylint: enable=too-many-arguments

    @property
    def key_count(self):
        """The number of keys that are being scanned. (read-only)"""
        return len(self.row_count) * len(self.col_count)

    def deinit(self):
        """Stop scanning and release the pins."""
        super().deinit()
        for row_dio in self._row_digitalinouts:
            row_dio.deinit()
        for col_dio in self._column_digitalinouts:
            col_dio.deinit()

    def reset(self):
        """
        Reset the internal state of the scanner to assume that all keys are now released.
        Any key that is already pressed at the time of this call will therefore immediately cause
        a new key-pressed event to occur.
        """
        self._previously_pressed = self._currently_pressed = [False] * self.key_count

    def _row_column_to_key_number(self, row, column):
        return (row * self.col_count) + column

    def _keypad_keymatrix_scan(self):
        for row, row_dio in enumerate(self._row_digitalinouts):
            row_dio.switch_to_output(
                value=(not self._columns_to_anodes),
                drive_mode=digitalio.DriveMode.PUSH_PULL,
            )
            for col, col_dio in enumerate(self._column_digitalinouts):
                key_number = self._row_column_to_key_number(row, col)
                self._previously_pressed[key_number] = self._currently_pressed[
                    key_number
                ]
                current = col_dio.value != self._columns_to_anodes
                self._currently_pressed[key_number] = current
                if self._previously_pressed[key_number] != current:
                    self._events.keypad_eventqueue_record(key_number, current)
            row_dio.value = self._columns_to_anodes
            row_dio.switch_to_input(
                pull=(
                    digitalio.Pull.UP
                    if self._columns_to_anodes
                    else digitalio.Pull.DOWN
                )
            )