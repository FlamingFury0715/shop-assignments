# dsSenateSense.py
# 1/18/19
# Phoenix Iserman
# detects if someone is elligible for senate

def main():
    age = eval(input("How old are you? "))
    years = eval(input("How long have you been a US citizen? "))
    if age > 25 and years > 7:
        if age > 30 and years > 9:
            print("You are elligible to be a US Senator and house representative.")
        else:
            print("You are elligible to be a house representative but not a US senator.")
            # I AM THE SENATE
    else:
        print("You are not elligible to be a house representative or US senator")

main()
