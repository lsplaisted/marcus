from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

import images, robot

def menu(programs: dict[int, (DriveBase, Motor, Motor)]):
    print("Creating hub")
    Robot = robot.Robot()
    hub = Robot.hub

    # Since we use the center button, this sets the combo of the center and bluetooth button to stop the program
    hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
    hub.light.on(Color.BLUE)

    selection = 0

    while True:
        
        stopped = False
        pressed = hub.buttons.pressed()
        if Button.RIGHT in pressed:
            selection += 1
            wait(200)
        if Button.LEFT in pressed:
            selection -= 1
            wait(200)
        if (selection < 0):
            selection = len(programs) - 1
        if selection > len(programs) - 1:
            selection = 0
        if Button.CENTER in pressed:
            hub.light.on(Color.MAGENTA)
            hub.display.animate(
                [
                    images.RUNNING_1,
                    images.RUNNING_2,
                    images.RUNNING_3,
                    images.RUNNING_4,
                    images.RUNNING_5,
                    images.RUNNING_6,
                    images.RUNNING_7,
                ],
                300,
            )

            # Default to not using the gyro, since that's the default for PyBricks block programming
            # It is recommended that each program start by turning the gyro on, but turning it off here
            # should keep results consistent
            Robot.drive_base.use_gyro(False)

            wait(500)
            
            try:
                # Set the stop button to just the center button, so we can use it to stop a running sub-program
                # We'll catch the SystemExit exception that is raised
                hub.system.set_stop_button([Button.CENTER])
                programs[selection](Robot.drive_base, Robot.left_attachment, Robot.right_attachment)
            except SystemExit:
                Robot.drive_base.stop()
                Robot.left_attachment.stop()
                Robot.right_attachment.stop()
                wait(500)
                stopped = True
            hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
            Robot.drive_base.stop()
            Robot.left_attachment.stop()
            Robot.right_attachment.stop()
            selection += 1
            # if selection > len(programs) - 1 and not stopped:
            #     celebrate.Run(br)
        hub.display.number(selection)
        hub.light.on(Color.GREEN)
