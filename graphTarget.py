# graphTarget.py
# 12/11/18
# Phoenix Iserman
# draws a target

from graphics import *

def main():
    win = GraphWin()
    cen = Point(100,100)
    #outermost white ring
    ringwhite = Circle(cen, 50)
    ringwhite.setFill('white')
    ringwhite.setOutline('black')
    ringwhite.draw(win)
    #black ring
    ringblack = Circle(cen, 40)
    ringblack.setFill('black')
    ringblack.draw(win)
    #blue ring
    ringblue = Circle(cen, 30)
    ringblue.setFill('blue')
    ringblue.draw(win)
    #red ring
    ringred = Circle(cen, 20)
    ringred.setFill('red')
    ringred.setOutline('black')
    ringred.draw(win)
    #bullseye
    bullseye = Circle(cen, 10)
    bullseye.setFill('yellow')
    bullseye.setOutline('black')
    bullseye.draw(win)

main()
