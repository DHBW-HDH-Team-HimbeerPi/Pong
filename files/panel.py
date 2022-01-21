

class Panel:
    def __init__(self, x: int, r: int, g: int, b: int):
        self.size = 4
        self.xPosition = x
        self.yPosition = 6
        self.r = r
        self.g = g
        self.b = b

    def moveUp(self):
        if self.xPosition > 0:
            self.xPosition - 1
            self.yPosition = self.xPosition + self.size

    def moveDown(self):
        if self.yPosition < 16:
            self.xPosition + 1
            self.yPosition = self.xPosition + self.size


    @property
    def getCoordinate(self):
        return (self.xPosition, self.yPosition)