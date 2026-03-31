from pybricks.hubs import PrimeHub
from pybricks.parameters import Button


class ButtonInput:
    """Tracks button state and detects new presses (rising edge)."""

    def __init__(self, hub: PrimeHub):
        self._hub = hub
        self._previous = set()
        self._just_pressed = set()

    def update(self):
        """Read current button state. Call once per loop iteration."""
        current = set(self._hub.buttons.pressed())
        self._just_pressed = current - self._previous
        self._previous = current

    def just_pressed(self, button: Button) -> bool:
        """True if button was pressed this update but not the previous one."""
        return button in self._just_pressed

    def is_held(self, button: Button) -> bool:
        """True if button is currently held down."""
        return button in self._previous
    
    def wait_until_released(self, button: Button):
        """Wait until the specified button is released."""
        while button in self._hub.buttons.pressed():
            pass
        # Sync internal state so the release doesn't register as a new press
        self._previous = set(self._hub.buttons.pressed())
