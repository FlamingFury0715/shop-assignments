# circum-pizzaedit.py
# made by Phoenix Iserman on 11/19/18
# calculates price per sq. in. of pizza

import math

def main():
    r = eval(input("what is the radius of the pizza in inches? ")) #gets variable for size of pizza
    A = math.pi * r ** 2 #size of pizza
    price = eval(input("How much are you paying for this pizza? ")) #finds price
    ans = price / A
    print("The pizza is worth $", ans, "per square inch")
    input("press any button to quit")

main()
