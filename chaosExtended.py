#ChaosExtended.py
#1/17/19
#Phoenix Iserman
#a simple program with chaotic behavior

def main():
    print("this program illustrates a chaotic function")
    x = eval(input("enter a number between 0 and 1: "))
    for i in range(20) :
        x = 2.0 * x * (1 - x)
        print(x)

main()
