class body(object):
    """An class which is used to store basic properties about a body"""

    def __init__(self, xPos, yPos, xVel, yVel, mass):
        """Create a new body

        xPos - The x component of the position
        yPos - The y component of the position
        xVel - The x component of the velocity
        yVel - The y component of the velocity
        mass - The mass of the body"""

        self.xPos = xPos
        self.yPos = yPos
        self.xVel = xVel
        self.yVel = yVel
        self.xAcl = 0.0
        self.yAcl = 0.0
        self.mass = mass
