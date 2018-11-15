# convert.py
# converts celsius to fahrenheit
# Phoenix Iserman

def main():
    x = eval(input("how many temperatures do you want to measure? "))
    for i in range (x):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9 / 5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
