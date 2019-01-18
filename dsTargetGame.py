# dsTargetGame.py
# 1/18/19
# Phoenix Iserman
# draws a target and lets the user play a game with it

from graphics import *

def main():
    win = GraphWin()
    #win.setCoords(-100.0, -100.0, 100.0, 100.0)
    cen = Point(100,100)
    score = 0
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


    #arrows
    for i in range(5):
        click = win.getMouse()
        cx = click.getX()
        cy = click.getY()
        arrow = Circle(click, 2)
        arrow.setFill("white")
        arrow.setOutline("black")
        arrow.draw(win)
        if 50 < cx < 150 and 50 < cy < 150:
            score += 1
            if 40 < cx < 140 and 40 < cy < 140:
                score += 2
                if 30 < cx < 130 and 30 < cy < 130:
                    score += 2
                    if 20 < cx < 120 and 20 < cy < 120:
                        score += 2
                        if 10 < cx < 110 and 10 < cy < 110:
                            score += 2
    print(score)

main()
