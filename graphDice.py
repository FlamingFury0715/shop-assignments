# graphDice.py
# Phoenix Iserman
# 12/11/18
# pulls up a straight of dice

from graphics import *

def main():
    win = GraphWin('Dice', 500, 100)
    #base dice
    dieback1 = Rectangle(Point(5, 5), Point(95, 95))
    dieback1.setFill('black')
    dieback1.draw(win)
    dieback2 = Rectangle(Point(105, 5), Point(195, 95))
    dieback2.setFill('black')
    dieback2.draw(win)
    dieback3 = Rectangle(Point(205, 5), Point(295, 95))
    dieback3.setFill('black')
    dieback3.draw(win)
    dieback4 = Rectangle(Point(305, 5), Point(395, 95))
    dieback4.setFill('black')
    dieback4.draw(win)
    dieback5 = Rectangle(Point(405, 5), Point(495, 95))
    dieback5.setFill('black')
    dieback5.draw(win)
    dieface1 = Rectangle(Point(15, 15), Point(85, 85))
    dieface1.setFill('white')
    dieface1.draw(win)
    dieface2 = Rectangle(Point(115, 15), Point(185, 85))
    dieface2.setFill('white')
    dieface2.draw(win)
    dieface3 = Rectangle(Point(215, 15), Point(285, 85))
    dieface3.setFill('white')
    dieface3.draw(win)
    dieface4 = Rectangle(Point(315, 15), Point(385, 85))
    dieface4.setFill('white')
    dieface4.draw(win)
    dieface5 = Rectangle(Point(415, 15), Point(485, 85))
    dieface5.setFill('white')
    dieface5.draw(win)
    #Dots on faces will be marked with two numbers. The first digit represents
    #the face that the marks are on. The second digit represents which mark it is.
    #first face
    dot11 = Rectangle(Point(45, 45), Point(55, 55))
    dot11.setFill('black')
    dot11.draw(win)
    #second face
    dot21 = Rectangle(Point(135, 35), Point(145, 45))
    dot21.setFill('black')
    dot21.draw(win)
    dot22 = Rectangle(Point(155, 55), Point(165, 65))
    dot22.setFill('black')
    dot22.draw(win)
    #third face
    dot31 = Rectangle(Point(225, 25), Point(235, 35))
    dot31.setFill('black')
    dot31.draw(win)
    dot32 = Rectangle(Point(245, 45), Point(255, 55))
    dot32.setFill('black')
    dot32.draw(win)
    dot33 = Rectangle(Point(265, 65), Point(275, 75))
    dot33.setFill('black')
    dot33.draw(win)
    #fourth face
    dot41 = Rectangle(Point(330, 30), Point(340, 40))
    dot41.setFill('black')
    dot41.draw(win)
    dot42 = Rectangle(Point(360, 60), Point(370, 70))
    dot42.setFill('black')
    dot42.draw(win)
    dot43 = Rectangle(Point(360, 30), Point(370, 40))
    dot43.setFill('black')
    dot43.draw(win)
    dot44 = Rectangle(Point(330, 60), Point(340, 70))
    dot44.setFill('black')
    dot44.draw(win)
    #fifth face
    dot51 = Rectangle(Point(425, 25), Point(435, 35))
    dot51.setFill('black')
    dot51.draw(win)
    dot52 = Rectangle(Point(445, 45), Point(455, 55))
    dot52.setFill('black')
    dot52.draw(win)
    dot53 = Rectangle(Point(465, 65), Point(475, 75))
    dot53.setFill('black')
    dot53.draw(win)
    dot54 = Rectangle(Point(465, 25), Point(475, 35))
    dot54.setFill('black')
    dot54.draw(win)
    dot55 = Rectangle(Point(425, 65), Point(435, 75))
    dot55.setFill('black')
    dot55.draw(win)

main()










