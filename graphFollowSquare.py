# graphFollowSquare
# 12/11/18
# Phoenix Iserman
# allows you to draw up to ten red squares before automatically closing

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(90,90))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        shape1 = shape.clone()
        shape1.draw(win)
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape1.move(dx,dy)
    center = Point(100,100)
    label = Text(center, "Click again to quit")
    label.draw(win)
    win.getMouse()
    win.close()

main()
