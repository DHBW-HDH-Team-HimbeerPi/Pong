from files.ball import Ball
from files.panel import Panel
from output_framework.output_framework import OutputFramework as oF
#from input_framework.imu_controller import IMUController
#from input_framework.interface import ThresholdType, TriggerMode
#from unicornhatsimulator import unicornhathd as uni
import numpy as np
import time


class Pong:

    def __init__(self):
        self.leftPanel = Panel(1, 0, 255, 0)
        self.rightPanel = Panel(14, 0, 0, 255)
        self.gameBall = Ball()
        self.speed = 0.01
        self.scoreLeft = 0
        self.scoreRight = 0
        self.play()

    def setGameItems(self, gameField, gameObject):
        xPosition = int (gameObject.xPosition)
        yPosition = int (gameObject.yPosition)
        size = gameObject.size
        for x in range(size):
            if yPosition < 16:
                gameField[xPosition][yPosition + x][0] = gameObject.r
                gameField[xPosition][yPosition + x][1] = gameObject.g
                gameField[xPosition][yPosition + x][2] = gameObject.b
        return gameField

    def play(self):
        while True:
            self.ballCheck()
            gameField = np.full((16, 16, 3), 0)
            gameField = self.setGameItems(gameField, self.leftPanel)
            gameField = self.setGameItems(gameField, self.rightPanel)
            gameField = self.setGameItems(gameField, self.gameBall)
            oF.setWindow(gameField)
            #for x in range(len(gameField)):
            #    for y in range(len(gameField[x])):
            #        uni.set_pixel(x, y, gameField[x][y][0], gameField[x][y][1], gameField[x][y][2])
            #uni.show()
            time.sleep(self.speed)

    def ballCheck(self):
        if int (self.gameBall.xPosition) <= 0 or int (self.gameBall.xPosition) >= 15:
            if int (self.gameBall.xPosition) == 0:
                self.scoreRight = self.scoreRight + 1
            else:
                self.scoreLeft = self.scoreLeft + 1
            self.leftPanel = Panel(1, 0, 255, 0)
            self.rightPanel = Panel(14, 0, 0, 255)
            self.gameBall = Ball()
        else:
            if int (self.gameBall.xPosition) == 1 or int (self.gameBall.xPosition) == 14:
                if int (self.gameBall.xPosition) == 1 and self.gameBall.yPosition >= self.leftPanel.yPosition and self.gameBall.yPosition <= (self.leftPanel.yPosition + self.leftPanel.size):
                    self.gameBall.panelBounce(self.leftPanel)
                else:
                    if int (self.gameBall.xPosition) == 14 and self.gameBall.yPosition >= self.rightPanel.yPosition and self.gameBall.yPosition <= (self.rightPanel.yPosition + self.rightPanel.size):
                        self.gameBall.panelBounce(self.leftPanel)
            if int (self.gameBall.yPosition) <= 0 or int (self.gameBall.yPosition) >= 15:
                self.gameBall.bounce()
            self.gameBall.move()

    def check(self):
        if True:
            if True:
                self.leftPanel.moveUp()
            else:
                self.leftPanel.moveDown()


if __name__ == "__main__":
    Pong()
