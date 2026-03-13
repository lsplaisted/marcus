from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
import images
import robot

def Run(robot: robot.Robot):
    robot.hub.display.animate(
                [
                    images.CLEAN_WHEELS_1,
                    images.CLEAN_WHEELS_2
                ],
                300,
            )
    robot.drive_base.use_gyro(False)
    robot.drive_base.settings(straight_speed=900)
    while True:
        robot.drive_base.straight(3000)

# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    bot = robot.Robot()
    Run(bot)