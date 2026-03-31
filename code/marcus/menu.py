from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from marcus.buttons import ButtonInput
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
    buttons = ButtonInput(hub)

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
            buttons.update()
            if buttons.just_pressed(Button.RIGHT):
                selection += 1
            if buttons.just_pressed(Button.LEFT):
                selection -= 1
            if (selection < 0):
                selection = len(programs) - 1
            if selection > len(programs) - 1:
                selection = 0
            if buttons.just_pressed(Button.CENTER):
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

                buttons.wait_until_released(Button.CENTER)
                
                try:
                    # Set the stop button to just the center button, so we can use it to stop a running sub-program
                    # We'll catch the SystemExit exception that is raised
                    hub.system.set_stop_button([Button.CENTER])
                    programs[selection](Robot.drive_base, Robot.left_attachment, Robot.right_attachment, Robot.hub)
                except SystemExit:
                    Robot.drive_base.stop()
                    Robot.left_attachment.stop()
                    Robot.right_attachment.stop()
                    buttons.wait_until_released(Button.CENTER)
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
                        pass
                    hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
                    Robot.hub.speaker.beep(1,1)
                    buttons.wait_until_released(Button.CENTER)
            hub.display.number(selection)
            hub.light.on(Color.GREEN)
            if buttons.just_pressed(Button.BLUETOOTH):
                mode = 1

        while mode == 1:
            buttons.update()
            if buttons.just_pressed(Button.RIGHT):
                option += 1
            if buttons.just_pressed(Button.LEFT):
                option -= 1
            if (option < 0):
                option = len(utilities) - 1
            if option > len(utilities) - 1:
                option = 0
            if buttons.just_pressed(Button.CENTER):
                hub.light.on(Color.BLUE)
                buttons.wait_until_released(Button.CENTER)
                try:
                    # Set the stop button to just the center button, so we can use it to stop a running sub-program
                    # We'll catch the SystemExit exception that is raised
                    hub.system.set_stop_button([Button.CENTER])
                    utilities[option][0](Robot)
                except SystemExit:
                    Robot.drive_base.stop()
                    Robot.left_attachment.stop()
                    Robot.right_attachment.stop()
                    buttons.wait_until_released(Button.CENTER)
            hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
            Robot.drive_base.stop()
            Robot.left_attachment.stop()
            Robot.right_attachment.stop()
            Robot.hub.speaker.beep(1,1)
            hub.display.icon(utilities[option][1])
            if buttons.just_pressed(Button.BLUETOOTH):
                mode = 0
