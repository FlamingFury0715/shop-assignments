#ChaosInput.py
#1/17/19
#Phoenix Iserman
#a simple program with chaotic behavior

def main():
    print("this program illustrates a chaotic function")
    x = eval(input("enter a number between 0 and 1: "))
    cycles = eval(input("How many times do you want the number to be looped? "))
    for i in range(cycles) :
        x = 2.0 * x * (1 - x)
        print(x)

main()
