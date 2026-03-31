from pybricks.tools import Matrix
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Color, Button
from pybricks.tools import wait
from marcus.images import STAR, STAR_2
import robot


def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, hub: PrimeHub):
    hub.display.animate([STAR, STAR_2], 200)
    hub.light.animate(
        (Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN), 200
    )
    hub.speaker.play_notes(
        [
            "G4/4",
            "G4/4",
            "E4/8",
            "G4/4",
            "E4/8",
            "G4/8",
            "E4/8",
            "D4/8",
            "G4/4",
            "R/8",
            "R/8",
            "G4/8",
            "D5/8",
            "E5/8",
            "D5/8",
            "E5/8",
            "D5/4",
            "C5/16",
            "B4/16",
            "A4/8",
            "G3/4",
            "A3/4",
            "G3/4",
            "G5/4",
        ],
        160,
    )
    hub.light.on(Color.MAGENTA)

    while(True):
        pass


# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    bot = robot.Robot()
    Run(bot.drive_base, bot.left_attachment, bot.right_attachment, bot.hub)