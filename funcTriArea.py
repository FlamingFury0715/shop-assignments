# funcTriArea.py
# Phoenix Iserman 1/16/19
# calculates area of a triangle given the length of the sides
#
# note: this may be a little off, because my computer froze up and
# closed all of my windows when I was editing the script, so I
# lost a lot of progress



from math import all

def area():
    a, b, c = eval(input("Please input the values of the sides, seperated by commas: "))
    s = (a + b + c) / 2
    A = sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area is", A)

def main():
    print("What are the measurements of the sides?")
    a, b, c = eval(input("Please input three values seperated by commas: "))
    s = (a + b + c) / 2
    A = sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area of the triangle is", A)
    input("Press <enter> to exit")

main()
