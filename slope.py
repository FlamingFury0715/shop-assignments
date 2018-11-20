# Slope.py
# Phoenix Iserman 11/20/18
# calculates slope from two values

def main():
    X1, Y1 = eval(input("What is the first set of coordinates, without parentheses? "))
    X2, Y2 = eval(input("What is the second set of coordinates, without parentheses? "))
    slope = (Y2 - Y1) / (X2 - X1)
    print("The slope of the given line is", slope)
    input("press the <enter> key to continue")

main()
