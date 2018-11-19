# circum.py
# made by Phoenix Iserman on 11/19/18
# calculates volume and surface area of a sphere

import math

def main():
    r = eval(input("what is the radius of the sphere? ")) #determines the radius of the sphere to be measured
    V = ((4 / 3) * math.pi * (r ** 3)) #determines volume
    A = (4 * math.pi * (r ** 2)) #determines s. area
    print("The volume of the sphere is", V, "and the surface area is", A)
    input("Press any button to exit")

main()
