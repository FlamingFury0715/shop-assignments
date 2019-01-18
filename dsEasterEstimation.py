# dsEasterEstimate.py
# 1/18/19
# Phoenix Iserman
# estimates the date of easter

from math import *

def main():
    print("The year input must be between 1981 and 2049")
    year = eval(input("What year do you want to find the date for? "))
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    if year > 2048 or year < 1982:
        print("Provided year is invalid")
    else:
        date = 22 + d + e
        month = "March"
        if date > 31:
            date -= 31
            month = "April"
        print("Easter will be on", month, date)
