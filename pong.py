from files.ball import Ball
from files.panel import Panel
#from output_framework.output_framework import OutputFramework as oF
import numpy as np
import time


class Pong:

    def __init__(self):
        self.leftPanel = Panel(1, 0, 255, 0)
        self.rightPanel = Panel(14, 0, 0, 255)
        self.gameBall = Ball()
        self.play()

    def setGameItems(self, gameField, gameObject):
        xPosition = gameObject.xPosition
        yPosition = gameObject.yPosition
        size = gameObject.size
        for x in range(size):
            gameField[xPosition][yPosition + x][0] = gameObject.r
            gameField[xPosition][yPosition + x][1] = gameObject.g
            gameField[xPosition][yPosition + x][2] = gameObject.b
        return gameField

    def play(self):
        while True:
            gameField = np.full((16, 16, 3), 255)
            gameField = self.setGameItems(gameField, self.leftPanel)
            gameField = self.setGameItems(gameField, self.rightPanel)
            gameField = self.setGameItems(gameField, self.gameBall)
#            oF.setWindow(gameField)
            time.sleep(1)


if __name__ == "__main__":
    Pong()
