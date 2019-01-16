# funcPizzaAreaCost
# 1/16/19
# Phoenix Iserman
# functions for calculating area of a pizza and the cost per square inch

from math import *
from numpy import *

def area(r):
    a = pi * r**2
    return(a)

def cost():
    x = eval(input("What is the radius of the pizza? "))
    mon = eval(input("What was the cost of the pizza? $"))
    area = eval(input("What is the area of the pizza? "))
    totalcost = mon / area
    print("The pizza cost", round(totalcost, 2), "per square inch")

def guide():
    print('To use this program, just type "cost()" and answer the given questions')



guide()
