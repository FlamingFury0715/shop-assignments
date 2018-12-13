# graphRuler.py
# Phoenix Iserman
# 12/12/18
# creates a digital ruler that has accurate inch markers
#
#
#------##IMPORTANT NOTE##------
#The Inches were calculated on a computer with a resolution of
#1920x1020, and a size of 24". Due to this, the size of the ruler may be
#inaccurate on screens with a diferent pixel density (PPI)

from graphics import *

def main():
    win = GraphWin('Ruler', 1101.456, 100)
    inch1 = Line(Point(91.788, 50), Point(91.788, 100))
    inch2 = Line(Point(183.576, 50), Point(183.576, 100))
    inch3 = Line(Point(275.364, 50), Point(275.364, 100))
    inch4 = Line(Point(367.152, 50), Point(367.152, 100))
    inch5 = Line(Point(458.94, 50), Point(458.94, 100))
    inch6 = Line(Point(550.728, 50), Point(550.728, 100))
    inch7 = Line(Point(642.516, 50), Point(642.516, 100))
    inch8 = Line(Point(734.304, 50), Point(734.304, 100))
    inch9 = Line(Point(826.092, 50), Point(826.092, 100))
    inch10 = Line(Point(917.88, 50), Point(917.88, 100))
    inch11 = Line(Point(1009.668, 50), Point(1009.668, 100))
    #inch12 = Line(Point(1101.456, 50), Point(1101.456, 100))
    #line 12 is excluded in the code because it's at the edge of the ruler
    #anyways, so it wouldn't normally be visible.


    inch1.draw(win)
    inch2.draw(win)
    inch3.draw(win)
    inch4.draw(win)
    inch5.draw(win)
    inch6.draw(win)
    inch7.draw(win)
    inch8.draw(win)
    inch9.draw(win)
    inch10.draw(win)
    inch11.draw(win)
    #inch12.draw(win)

main()
