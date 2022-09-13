"""Python implementation of the keypad library. Borrowed code from the Blinka library"""

from collections import deque
from keypad import Event

class EventQueue:
    """
    A queue of `Event` objects, filled by a `keypad` scanner such as `Keys` or `KeyMatrix`.

    You cannot create an instance of `_EventQueue` directly. Each scanner creates an
    instance when it is created.
    """

    def __init__(self, max_events):
        self._events = deque((), max_events)
        self._max_events=max_events
        self._overflowed = False

    def get(self):
        """
        Return the next key transition event. Return ``None`` if no events are pending.

        Note that the queue size is limited; see ``max_events`` in the constructor of
        a scanner such as `Keys` or `KeyMatrix`.
        If a new event arrives when the queue is full, the event is discarded, and
        `overflowed` is set to ``True``.

        :return: the next queued key transition `Event`
        :rtype: Optional[Event]
        """
        if not self._events:
            return None
        return self._events.popleft()

    def get_into(self, event):
        """Store the next key transition event in the supplied event, if available,
        and return ``True``.
        If there are no queued events, do not touch ``event`` and return ``False``.

        The advantage of this method over ``get()`` is that it does not allocate storage.
        Instead you can reuse an existing ``Event`` object.

        Note that the queue size is limited; see ``max_events`` in the constructor of
        a scanner such as `Keys` or `KeyMatrix`.

        :return ``True`` if an event was available and stored, ``False`` if not.
        :rtype: bool
        """
        if not self._events:
            return False
        next_event = self._events.popleft()
        # pylint: disable=protected-access
        event._key_number = next_event._key_number
        event._pressed = next_event._pressed
        # pylint: enable=protected-access
        return True

    def clear(self):
        """
        Clear any queued key transition events. Also sets `overflowed` to ``False``.
        """
        self._events.clear()
        self._overflowed = False

    def __bool__(self):
        """``True`` if `len()` is greater than zero.
        This is an easy way to check if the queue is empty.
        """
        return len(self._events) > 0

    def __len__(self):
        """Return the number of events currently in the queue. Used to implement ``len()``."""
        return len(self._events)

    @property
    def overflowed(self):
        """
        ``True`` if an event could not be added to the event queue because it was full. (read-only)
        Set to ``False`` by  `clear()`.
        """
        return self._overflowed

    def keypad_eventqueue_record(self, key_number, current):
        """Record a new event"""
        if len(self._events) == self._max_events:
            self._overflowed = True
        else:
            self._events.append(Event(key_number, current))