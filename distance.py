# Distance.py
# Phoenix Iserman 11/20/18
# calculates distance between two points

import math

def main():
    X1, Y1 = eval(input("What is the first set of coordinates, without parentheses? "))
    X2, Y2 = eval(input("What is the second set of coordinates, without parentheses? "))
    distance = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2 )
    print("The distance between points is", distance, "units.")
    input("press the <enter> key to continue")

main()
