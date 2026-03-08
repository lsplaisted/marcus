from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor):
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(695)
    drive_base.turn(-45)
    drive_base.straight(300)
    drive_base.straight(-300)
    drive_base.turn(75)
    drive_base.straight(-735)


# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(robot.drive_base, robot.left_attachment, robot.right_attachment)