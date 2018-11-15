# convert.py
# converts celsius to fahrenheit
# Phoenix Iserman

def main():
    x = -10
    for i in range (10):
        x = x + 10
        celsius = x + 10
        fahrenheit = 9 / 5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit, or", celsius, "degrees Celsius")

main()
