# dsChaos.py
# 1/18/19
# Phoenix Iserman
# a simple program with chaotic behavior
# Used for the last question on 3.1

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    if 0 < x < 1:
        for i in range(10) :
            x = 3.9 * x * (1 - x)
            print(x)
    else:
        print("Invalid input")

main()
