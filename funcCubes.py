# funcCubes.py
# 1/16/19
# Phoenix Iserman
# gives the sum of numbers and their cubes

from math import *
from numpy import*

def sumN(n):
    tempo = 0
    total = 0
    for i in range(n):
        tempo += 1
        total += tempo
    print("The total is", total)

def cubicSumN(n):
    tempo = 0
    sqtempo = 0
    total = 0
    for i in range(n):
        tempo += 1
        sqtempo = tempo**2
        total += sqtempo
    print("The total is", total)

def guide():
    print('To use this program, type sumN(n) or cubicSumN(n), with "n"')
    print("being replaced with the number you wish to go up to.")

guide()
