# graphFlag.py
# Phoenix Iserman
# 12/12/18
# makes a flag

from graphics import *

def main():
    win = GraphWin('New Atlantis Flag', 240, 240)
    win.setBackground("blue4")
    tri = Polygon(Point(120, 200), Point(25, 45), Point(215, 45))
    tri.setFill(color_rgb(184, 134, 11))
    tri.setWidth(3)
    tri.setOutline('white')
    tri.draw(win)
    hole = Circle(Point(120, 107.5), 17.5)
    hole.setFill('blue4')
    hole.setWidth(1.5)
    hole.setOutline('white')
    hole.draw(win)
    


main()
