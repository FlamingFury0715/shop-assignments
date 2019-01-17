#Chaos.py
#1/17/19
#Phoenix Iserman
#a simple program with chaotic behavior

def main():
    print("this program illustrates a chaotic function")
    x = eval(input("enter a number between 0 and 1: "))
    for i in range(10) :
        x = 3.9 * x * (1 - x)
        print(x)

def calc1():
    print("this program illustrates a chaotic function")
    x = eval(input("enter a number between 0 and 1: "))
    for i in range(10) :
        x = 3.9 * x * (1 - x)
        print(x)
        
def calc2():
    print("this program illustrates a chaotic function")
    x = eval(input("enter a number between 0 and 1: "))
    for i in range(10) :
        x = 3.9 * (x - x * x)
        print(x)

def calc3():
    print("this program illustrates a chaotic function")
    x = eval(input("enter a number between 0 and 1: "))
    for i in range(10) :
        x = 3.9 * x - 3.9 * x * x
        print(x)

main()
