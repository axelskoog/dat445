Write the class `Robot` which models the state of a robot which moves over a surface. It follows three commands: `turnLeft()`, `turnRight()` and `forward(n)`.
The first two commands tell the robot to turn to the left/right while the last tells it to go forward with `n` number of steps.

The class must maintain the current coordinates of the robot and its direction. The direction is one of the strings: `'NORTH'`, `'SOUTH'`, `'EAST'`, `'WEST'`, and indicates which world direction the robot is currently facing. The class must have the methods `turnLeft()`, `turnRight()` and `forward(n)` as well as:

* `__init__(self)`: which sets the current coordinates to be `x=0` and `y=0` and the initial direction to be `'NORTH'`.
* `getPosition(self)`: which returns the current position as the tuple `(x, y)`.
* `getDirection(self)`: which returns the current direction as a string.
