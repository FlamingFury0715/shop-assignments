# triarea.py
# Phoenix Iserman 11/20/18
# calculates area of a triangle given the length of the sides

import math

def main():
    input("What are the measurements of the sides?")
    a, b, c = eval(input("Please input three values seperated by commas: "))
    s = (a + b + c) / 2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area of the triangle is", A)
    input("Press <enter> to exit")

main()
