# WordLengthAverage.py
# Phoenix Iserman
# 1/2/19
# calculates the average length of words in a phrase

from math import *

def main():
    count1 = 0
    usrinput = input("What do you want to say? ")
    wc = eval(input("How many words are in the statement? "))
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for char in chars:
        count = usrinput.count(char)
        count1 += count
    print("character count is", count1)
    average = (count1 // wc)
    print(average)
    
    



main()
