# graphSnowman.py
# Phoenix Iserman
# 12/11/18
# a program that draws a snowman and a christmas tree

from graphics import *

def main():
    win = GraphWin('Window', 750.0, 500.0)
    ground = Rectangle(Point(0, 400), Point(750, 500))
    ground.setFill('white')
    ground.draw(win)
    #Tree building
    trunk = Rectangle(Point(225, 475), Point(275, 350))
    trunk.setFill('brown')
    trunk.draw(win)
    treetierbot = Polygon(Point(250, 225), Point(125, 350), Point(375, 350))
    treetierbot.setFill('green')
    treetierbot.setOutline('green')
    treetierbot.draw(win)
    treetiermid = Polygon(Point(250, 150), Point(135, 275), Point(365, 275))
    treetiermid.setFill('green')
    treetiermid.setOutline('green')
    treetiermid.draw(win)
    treetiertop = Polygon(Point(250, 75), Point(145, 200), Point(355, 200))
    treetiertop.setFill('green')
    treetiertop.setOutline('green')
    treetiertop.draw(win)
    #snowman body building
    #and no, not going to the gym
    lowball = Point(550, 375)
    midball = Point(550, 260)
    topball = Point(550, 160)
    snowtierbot = Circle(lowball, 75)
    snowtierbot.setFill('white')
    snowtierbot.draw(win)
    snowtiermid = Circle(midball, 65)
    snowtiermid.setFill('white')
    snowtiermid.draw(win)
    snowtiertop = Circle(topball, 55)
    snowtiertop.setFill('white')
    snowtiertop.draw(win)
    snowfixlow = Rectangle(Point(510, 310), Point(590, 325))
    snowfixlow.setFill('white')                       
    snowfixlow.setOutline('white')
    snowfixlow.draw(win)
    snowfixhi = Rectangle(Point(518, 200), Point(582, 225))
    snowfixhi.setFill('white')
    snowfixhi.setOutline('white')
    snowfixhi.draw(win)
    #snowman's face
    lcoal = Point(530, 145)
    rcoal = Point(570, 145)
    leye = Circle(lcoal, 5)
    leye.setFill('black')
    leye.draw(win)
    reye = Circle(rcoal, 5)
    reye.setFill('black')
    reye.draw(win)
    nose = Polygon(Point(550, 175), Point(557, 150), Point(543, 150))
    nose.setFill('orange2')
    nose.draw(win)
    
main()
