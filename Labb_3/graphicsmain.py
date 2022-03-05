#!/usr/bin/env python3

# !DISCLAIMER!
# Do NOT submit this code as your own.
# Submissions will be checked for plagiarism.
# Offenders will not be able to pass the course.

import os
import sys
sys.dont_write_bytecode = True  # noqa
from gamemodel import *
from graphics import *


def jank(n):
    i = n.__int__()
    return n if n != i else i


def linspace(start, stop, n):
    if n < 0:
        return []
    if n == 1:
        return [stop]
    h = (stop - start) / (n - 1)
    return [start+h*i for i in range(n)]


class ExtendedGraphWin(GraphWin):
    def raiseWindow(self, topmost=True):
        self.master.attributes("-topmost", topmost)
        self.master.lift()


class EaseInOut:
    def __init__(self, start=0, end=1, duration=1):
        self.start = start
        self.end = end
        self.duration = duration

    @staticmethod
    def func(t):
        if t < 0.5:
            return 2 * t * t
        return (-2 * t * t) + (4 * t) - 1

    def ease(self, alpha):
        t = alpha / self.duration
        a = self.func(t)
        return self.end * a + self.start * (1 - a)

    def __call__(self, alpha):
        return self.ease(alpha)


class GameGraphics:
    def __init__(self, game):
        angle, speed = game.getCurrentPlayer().getAim()
        wind = game.getCurrentWind()

        self.game = game

        # open the window
        self.win = ExtendedGraphWin("Cannon Game", 640, 480, autoflush=False)
        self.win.setCoords(-110, -10, 110, 155)
        self.win.raiseWindow(False)

        # open the input dialog
        self.inp = InputDialog(angle, speed, wind)
        self.inp.raiseWindow()

        # draw the terrain
        Line(Point(-110, 0), Point(110, 0)).draw(self.win)

        self.draw_cannons = [self.drawCanon(0), self.drawCanon(1)]
        self.draw_scores = [self.drawScore(0), self.drawScore(1)]
        self.draw_projs = [None, None]

    def drawCanon(self, playerNr):
        player = self.game.getPlayers()[playerNr]
        size = self.game.getCannonSize() / 2.0

        up_left = Point(player.getX() - size, player.getY() + size)
        down_righ = Point(player.getX() + size, player.getY() - size)

        cube_rect = Rectangle(up_left, down_righ)
        cube_rect.setFill(player.getColor())

        return cube_rect.draw(self.win)

    def drawScore(self, playerNr):
        p = self.game.getPlayers()[playerNr]
        x, y = p.getX(), p.getY()-self.game.getCannonSize() / 2.0 - 5.0
        t = Text(Point(x, y), f'Score: {p.getScore()}')
        return t.draw(self.win)

    def fire(self, angle, vel):
        player = self.game.getCurrentPlayer()
        index = self.game.getCurrentPlayerNumber()
        projs = self.draw_projs
        proj = player.fire(angle, vel)

        ball_X, ball_Y = proj.getX(), proj.getY()

        if projs[index]:
            projs[index].undraw()

        ball = Circle(Point(ball_X, ball_Y), self.game.getBallSize())
        ball.setFill(player.getColor())
        projs[index] = ball.draw(self.win)

        self.win.raiseWindow()
        self.inp.raiseWindow(False)

        while proj.isMoving():
            proj.update(1/50)
            ball.move(proj.getX() - ball_X, proj.getY() - ball_Y)
            ball_X, ball_Y = proj.getX(), proj.getY()
            update(50)

        return proj

    def updateScore(self, playerNr):
        score = self.draw_scores[playerNr]
        value = self.game.getPlayers()[playerNr].getScore()
        score.undraw()
        score.setText(f"Score: {value}")
        score.draw(self.win)

    def gameloop(self):
        while self.win.isOpen():
            player = self.game.getCurrentPlayer()
            opponent = self.game.getOtherPlayer()

            # retrieve this player's previous settings
            angle, speed = player.getAim()
            self.inp.setValues(angle, speed)

            self.win.raiseWindow(False)
            action = self.inp.interact()

            if action == "Fire!":
                angle, speed = self.inp.getValues()
            else:
                return os.EX_OSERR

            proj = self.fire(angle, speed)
            dist = opponent.projectileDistance(proj)

            if not dist:  # bool(0.0) => False
                player.increaseScore()
                self.explode()
                self.updateScore(self.game.getCurrentPlayerNumber())
                self.game.newRound()

            self.game.nextPlayer()

    def play(self):
        try:
            self.gameloop()
        except GraphicsError:
            pass
        except KeyboardInterrupt:
            pass
        return os.EX_OSERR

    def explode(self):
        other = self.game.getOtherPlayer()
        color = self.game.getCurrentPlayer().getColor()
        centr = Point(other.getX(), other.getY())
        ease = EaseInOut(start=self.game.getBallSize(),
                         end=self.game.getCannonSize()*2,
                         duration=1
                         )
        rad = linspace(0, 1, 1000//50)
        for radius in map(ease, rad):
            circle = Circle(centr, radius)
            circle.setWidth(0)
            circle.setFill(color)
            circle.draw(self.win)
            update(50)
            circle.undraw()


class InputDialog:
    def __init__ (self, angle, vel, wind):
        self.win = win = ExtendedGraphWin("Fire", 200, 300)
        win.setCoords(0, 4.5, 4, 0.5)
        Text(Point(1, 1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1, 2), "Velocity").draw(win)
        self.vel = Entry(Point(3, 2), 5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1, 3), "Wind").draw(win)
        self.height = Text(Point(3, 3), 5).draw(win)
        self.height.setText("{0:.2f}".format(wind))

        self.fire = Button(win, Point(1, 4), 1.25, .5, "Fire!")
        self.fire.activate()
        self.quit = Button(win, Point(3, 4), 1.25, .5, "Quit")
        self.quit.activate()

    def interact(self):
        self.win.raiseWindow()
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    def getValues(self):
        try:
            a = float(self.angle.getText())
            v = float(self.vel.getText())
        except ValueError:
            a = Game.INITIAL_ANGLE
            v = Game.INITIAL_VELOCITY
        return a, v

    def setValues(self, angle, vel):
        self.angle.setText(str(jank(angle)))
        self.vel.setText(str(jank(vel)))
        if self.win.isOpen():
            self.win.redraw()

    def close(self):
        if not self.win.isClosed():
            self.win.close()

    def raiseWindow(self, topmost=True):
        self.win.raiseWindow(topmost)


class Button:
    def __init__(self, win, center, width, height, label):
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = 0
        self.deactivate()

    def clicked(self, p):
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0


if __name__ == "__main__":
    game = Game(11, 3)
    graph = GameGraphics(game)
    try:
        ret = graph.play()
    except Exception as err:
        ret = os.EX_OSERR
        print(f"Error: {err}")
    # assuming no additional exception handler will catch SystemExit
    sys.exit(ret)
