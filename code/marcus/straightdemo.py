from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
import robot

def Run(robot: robot.Robot):
    robot.drive_base.use_gyro(True)
    robot.drive_base.settings(straight_speed=900)
    robot.drive_base.straight(3000)

# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    bot = robot.Robot()
    Run(bot)