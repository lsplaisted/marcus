from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Button


class ButtonInput:
    """Tracks button state and detects new presses (rising edge).
    Optionally treats a force sensor press as a Center button press."""

    def __init__(self, hub: PrimeHub, force_sensor: ForceSensor = None):
        self._hub = hub
        self._force_sensor = force_sensor
        self._previous = set()
        self._just_pressed = set()

    def _read_buttons(self):
        """Read hub buttons, adding CENTER if force sensor is pressed."""
        current = set(self._hub.buttons.pressed())
        if self._force_sensor and self._force_sensor.pressed():
            current.add(Button.CENTER)
        return current

    def update(self):
        """Read current button state. Call once per loop iteration."""
        current = self._read_buttons()
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
        while button in self._read_buttons():
            pass
        # Sync internal state so the release doesn't register as a new press
        self._previous = self._read_buttons()
