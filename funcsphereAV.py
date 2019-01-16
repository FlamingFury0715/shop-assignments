# funcsphereAV.py
# 1/16/19
# Phoenix Iserman
# contains functions for the area and volume of a sphere

from math import *

def sphereArea(r):
    area = 4 * pi * r**2
    print("The surface area of the given sphere is", area, "units^2")

def sphereVolume(r):
    volume = 4 / 3 * pi * r**3
    print("The volume of the given sphere is", volume, "units^3")

def guide():
    print('To use this program, type sphereVolume(r) or sphereArea(r),')
    print('where "r" represents the radius of the sphere. Just replace')
    print('the "r" with the number!')

guide()
