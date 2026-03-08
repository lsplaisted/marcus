from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
import robot

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor):
    drive_base.settings(straight_speed=450)
    drive_base.straight(810, then=Stop.COAST)
    drive_base.arc(15, angle=-45, then=Stop.COAST)
    drive_base.straight(40, then=Stop.COAST)
    drive_base.arc(15, angle=-45, then=Stop.COAST)
    drive_base.straight(15, then=Stop.COAST)
    drive_base.turn(90, then=Stop.COAST)
    drive_base.straight(-300, then=Stop.NONE)
    drive_base.arc(500, angle=-45, then=Stop.NONE)

# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(robot.drive_base, robot.left_attachment, robot.right_attachment)