

class Ball:

    def __init__(self):
        self.xPosition = 7
        self.yPosition = 7
        self.size = 1
        self.r = 255
        self.g = 255
        self.b = 255

    @property
    def getCoordinate(self):
        return (self.xPosition, self.yPosition)