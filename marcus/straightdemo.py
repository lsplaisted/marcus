from pybricks.parameters import Direction, Port, Stop
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor, hub: PrimeHub):
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(3000)

# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    bot = robot.Robot()
    Run(bot.drive_base, bot.left_attachment, bot.right_attachment, bot.hub)