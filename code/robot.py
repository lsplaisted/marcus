from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Axis
from pybricks.robotics import DriveBase

TIRE_DIAMETER = 56  # mm - Large spike tires - 88 mm, small spike tires - 56 mm, projekt alpha tires 62.4 mm

AXLE_TRACK = (
    18 * 8
)  # distance between the wheels, mm - 16 studs * 8 mm each stud

class Robot():
    def __init__(self):
        # If your hub's screen doesn't face upwards, do something like this:
        # self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)        
        self.hub = PrimeHub()

        # Update ports and directions here as appropriate
        self.left_wheel = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        self.right_wheel = Motor(Port.F, Direction.CLOCKWISE)
        self.left_attachment = Motor(Port.A, Direction.CLOCKWISE)
        self.right_attachment = Motor(Port.B, Direction.CLOCKWISE)

        self.drive_base = DriveBase(self.left_wheel, self.right_wheel, TIRE_DIAMETER, AXLE_TRACK)