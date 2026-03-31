from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from marcus.celebrate import Run as celebrate_Run
from marcus.cleanwheels import Run as cleanwheels_Run
from marcus.battery import Run as battery_Run
from marcus.straightdemo import Run as straightdemo_Run
from marcus.images import *
import robot

def menu(programs):
    menu2(programs)

def menu2(programs: list[object]):
    Robot = robot.Robot()
    hub = Robot.hub

    utilities = [
        (cleanwheels_Run, CLEAN_WHEELS_1),
        (battery_Run, BATTERY),
        (celebrate_Run, STAR),
        (straightdemo_Run, UP_ARROW),
    ]

    # Since we use the center button, this sets the combo of the center and bluetooth button to stop the program
    hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
    hub.light.on(Color.BLUE)

    selection = 0
    option = 0
    mode = 0

    print("M.A.R.C.U.S. Ready")

    while True:
        while mode == 0:
            
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
                        RUNNING_1,
                        RUNNING_2,
                        RUNNING_3,
                        RUNNING_4,
                        RUNNING_5,
                        RUNNING_6,
                        RUNNING_7,
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
                if selection > len(programs) - 1 and not stopped:
                    try:
                        hub.system.set_stop_button([Button.CENTER])
                        celebrate_Run(Robot)
                    except SystemExit:
                        wait(500)
                    hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
            hub.display.number(selection)
            hub.light.on(Color.GREEN)
            if Button.BLUETOOTH in pressed:
                mode = 1
                wait(500)

        while mode == 1:
            pressed = hub.buttons.pressed()
            if Button.RIGHT in pressed:
                option += 1
                wait(200)
            if Button.LEFT in pressed:
                option -= 1
                wait(200)
            if (option < 0):
                option = len(utilities) - 1
            if option > len(utilities) - 1:
                option = 0
            if Button.CENTER in pressed:
                hub.light.on(Color.BLUE)
                wait(500)
                try:
                    # Set the stop button to just the center button, so we can use it to stop a running sub-program
                    # We'll catch the SystemExit exception that is raised
                    hub.system.set_stop_button([Button.CENTER])
                    utilities[option][0](Robot)
                except SystemExit:
                    Robot.drive_base.stop()
                    Robot.left_attachment.stop()
                    Robot.right_attachment.stop()
                    wait(1000)
            hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
            Robot.drive_base.stop()
            Robot.left_attachment.stop()
            Robot.right_attachment.stop()
            Robot.hub.speaker.beep(1,1)
            hub.display.icon(utilities[option][1])
            if Button.BLUETOOTH in pressed:
                mode = 0
                wait(500)
