#ChaosTable.py
#recreated 2/12/15 by Phoenix Iserman
#a simple program with chaotic behavior

def main():
    z = 0
    print("this program illustrates a chaotic function")
    x, y = eval(input("enter two numbers between 0 and 1, seperated by a comma: "))
    waves = eval(input("how many times do you want this to go through? "))
    print("Index       ", x, "       ", y)
    print("---------------------------------")
    for i in range(waves):
        z += 1
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(" ", z, "        ", round(x, 6), "  ", round(y, 6))

main()
