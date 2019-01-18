# dsBMICalc.py
# 1/17/19
# Phoenix Iserman
# calculates someone's BMI based on their input

from math import *

def main():
    w = eval(input("What is your weight? "))
    h = eval(input("What is your height in inches? "))
    tw = w * 720
    hsq = h**2
    BMI = tw / hsq
    if BMI > 25:
        result = "above"
    else:
        if BMI < 19:
            result = "below"
        else:
            result = "within"
    print("Your BMI is", result, "the healthy range")
    #print(BMI)

main()
