
# !DISCLAIMER!
# Do NOT submit this code as your own.
# Submissions will be checked for plagiarism.
# Offenders will not be able to pass the course.

from math import sin, cos, radians
from operator import add, sub
import random


class Game:
    UPPER_LIMIT = +110
    LOWER_LIMIT = -110

    INITIAL_VELOCITY = 40.0
    INITIAL_ANGLE = 45.0

    def __init__(self, cannonSize, ballSize):
        self.cannon_size = cannonSize
        self.ball_size = ballSize
        self.player_ind = 0
        self.wind = 0
        self.newRound()
        self.players = [
            Player(self, Game.INITIAL_ANGLE, [-90, 0], 'blue'),
            Player(self, Game.INITIAL_ANGLE, [+90, 0], 'red')
        ]

    def getPlayers(self):
        return self.players

    def getCannonSize(self):
        return self.cannon_size

    def getBallSize(self):
        return self.ball_size

    def getCurrentPlayer(self):
        return self.players[self.player_ind]

    def getOtherPlayer(self):
        return self.players[self.player_ind ^ 1]

    def getCurrentPlayerNumber(self):
        return self.player_ind

    def nextPlayer(self):
        self.player_ind ^= 1

    def setCurrentWind(self, wind):
        self.wind = wind

    def getCurrentWind(self):
        return self.wind

    def newRound(self):
        self.wind = random.random() * 10.0 * random.choice([-1.0, 1.0])


class Player:
    def __init__(self, game: Game, angle, pos, color):
        self.color = color
        self.pos = pos
        self.velocity = Game.INITIAL_VELOCITY
        self.angle = angle
        self.game = game
        self.score = 0

    def fire(self, angle, velocity):
        self.angle = angle
        self.velocity = velocity
        return Projectile(180 - angle if self.isPlayer2() else angle,
                          velocity,
                          self.game.getCurrentWind(),
                          self.getX(),
                          self.getY(),
                          Game.LOWER_LIMIT,
                          Game.UPPER_LIMIT
                          )

    def projectileDistance(self, proj):
        dist = proj.getX() - self.getX()
        oper = add if dist < 0 else sub
        marg = self.game.getCannonSize() / 2.0 + self.game.getBallSize()
        return 0 if abs(dist) <= marg else oper(dist, marg)

    def getScore(self):
        return self.score

    def increaseScore(self):
        self.score += 1

    def getColor(self):
        return self.color

    def getX(self):
        return self.pos[0]

    def getY(self):
        return self.pos[1] + self.game.getCannonSize() / 2.0

    def getAim(self):
        return self.angle, self.velocity

    def isPlayer2(self) -> bool:
        return self.game.players[1] is self


class Projectile:
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind

    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time

        # Move based on the average velocity in the time period
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0

        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)

        # Make sure xLower <= xPos <= mUpper
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)

        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1

    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos
