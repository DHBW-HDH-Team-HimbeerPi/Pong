from files.ball import Ball
from files.panel import Panel
import numpy as np

class Pong:

    def __init__(self):
        self.leftPanel = Panel(1, 0, 255, 0)
        self.rightPanel = Panel(14, 0, 0, 255)
        self.gameBall = Ball()


    def setGameItems(self, gameField, panel):
        xPosition, yPosition = panel.getCoordinate()
        size = panel.size
        for x in range(size):
            gameField[xPosition][yPosition + x][0] = panel.r
            gameField[xPosition][yPosition + x][1] = panel.g
            gameField[xPosition][yPosition + x][2] = panel.b
        return gameField

    def play(self):

        while True:
            gameField = np.full((16, 16, 3), 0)
            gameField = self.setGameItems(gameField, self.leftPanel)
            gameField = self.setGameItems(gameField, self.rightPanel)
            gameField = self.setGameItems(gameField, self.gameBall)
