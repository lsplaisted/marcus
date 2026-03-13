from pybricks.tools import Matrix
import robot
import images
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.tools import wait

def Rescale(val, in_min, in_max, out_min, out_max):
    neg = val / abs(val)  # will either be 1 or -1
    val = abs(val)
    if in_max == in_min:
        return 0
    if val < in_min:
        val = in_min
    if val > in_max:
        val = in_max
    retVal = out_min + (val - in_min) * (
        (out_max - out_min) / (in_max - in_min)
    )
    if retVal > out_max:
        retVal = out_max
    if retVal < out_min:
        retVal = out_min
    return retVal * neg

def RescaleBatteryVoltage(volts):
    return Rescale(volts, 7000, 8000, 0, 100)


def Run(robot: robot.Robot):
    while True:
        v = robot.hub.battery.voltage()
        vPct = RescaleBatteryVoltage(v)
        robot.hub.display.number(vPct)



# Don't modify the code below
# It runs the Run method if this file is run directly (not from the master program)
if __name__ == "__main__":
    bot = robot.Robot()
    Run(bot)
