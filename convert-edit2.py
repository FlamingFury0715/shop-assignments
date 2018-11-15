# convert.py
# converts celsius to fahrenheit
# Phoenix Iserman

def main():
    input("This program converts the temperature in Celsuis to Fahrenheit! press any key to continue")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press any key to exit.")

main()
