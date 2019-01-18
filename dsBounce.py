# dsBounce.py
# 1/18/19
# Phoenix Iserman
# makes a ball bounce around the screen

from graphics import *
import time, random

def bounceInBox(shape, dx, dy, xLow, xHigh, yLow, yHigh):
    
    delay = .005
    for i in range(6000):
        shape.move(dx, dy)
        center = shape.getCenter()
        x = center.getX()
        y = center.getY()
        if x < xLow:
            dx = -dx
        elif x > xHigh:
            dx = -dx
        if y < yLow:
            dy = -dy
        elif y > yHigh:
            dy = -dy            
        time.sleep(delay)

def getRandomPoint(xLow, xHigh, yLow, yHigh):
    x = random.randrange(xLow, xHigh+1)
    y = random.randrange(yLow, yHigh+1)
    return Point(x, y)   

def makeDisk(center, radius, win):
    disk = Circle(center, radius)
    disk.setOutline("red")
    disk.setFill("red")
    disk.draw(win)
    return disk

def bounceBall(dx, dy):
    
    winWidth = 290
    winHeight = 290
    win = GraphWin('Ball Bounce', winWidth, winHeight)
    win.setCoords(0,0,winWidth, winHeight)

    radius = 10
    xLow = radius 
    xHigh = winWidth - radius
    yLow = radius
    yHigh = winHeight - radius

    center = getRandomPoint(xLow, xHigh, yLow, yHigh)
    ball = makeDisk(center, radius, win)
    
    bounceInBox(ball, dx, dy, xLow, xHigh, yLow, yHigh)    

    win.close()
    
bounceBall(3, 5)
