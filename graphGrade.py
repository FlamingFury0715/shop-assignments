# graphGrade.py
# Phoenix Iserman
# 1/4/19
# creates a bar graph of grades entered in a file
# test file is gradetestr

from graphics import *

def main():
    file = input("Please enter the name of the file with grades: ")
    fileopen = open(file, 'r')
    studentnum = sum(1 for line in open(file))
    currstudnum = 0
    height = studentnum * 100
    win = GraphWin('Scores', 400, 700)
    win.setCoords(-175.0, -50.0, 500.0, 1000.0)
    yax = Line(Point(250.0, 0.0), Point(0.0, 0.0))
    xax = Line(Point(0.0, 0.0), Point(0.0, height))
    yax.draw(win)
    xax.draw(win)
    #number marker lines
    markfail = Line(Point(50.0, 0.0), Point(50.0, height))
    markfail.setFill('red')
    markfail.draw(win)
    markhalf = Line(Point(100.0, 0.0), Point(100.0, height))
    markhalf.setFill('orange')
    markhalf.draw(win)
    markpass = Line(Point(150.0, 0.0), Point(150.0, height))
    markpass.setFill('yellow')
    markpass.draw(win)
    markperfect = Line(Point(200.0, 0.0), Point(200.0, height))
    markperfect.setFill('green')
    markperfect.draw(win)
    #number marker text
    Text(Point(50.0, -12.5), '25').draw(win)
    Text(Point(100.0, -12.5), '50').draw(win)
    Text(Point(150.0, -12.5), '75').draw(win)
    Text(Point(200.0, -12.5), '100').draw(win)
    #bar placement
    for i in range(studentnum):
        currstudnum += 1
        temp = fileopen.readline()
        name, score = temp.split(" ")
        scorebar = int(score) * 2
        barheight = Rectangle(Point(0.0, (10.0 + (50 * currstudnum))), Point(scorebar, (40.0 + (50 * currstudnum))))
        barheight.setFill('white')
        barheight.draw(win)
        Text(Point(-70.0, 25.0 + (50 * currstudnum)), name).draw(win)

main()
