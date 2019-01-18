# dsWages.py
# 1/17/19
# Phoenix Iserman
# Calculates wages for time-and-a-half
# minimum wage locally is $12.00 as of writing this script and is the
# test amount

def main():
    hrs = eval(input("How many hours did you work over the past week? "))
    pay = eval(input("What is your hourly wage? "))
    overpay = pay / 2
    overtime = 0
    overtotal = 0
    overhours = 0
    if hrs > 40:
        overhours = hrs - 40
        overtime = overhours - 40
        overtotal = overtime * overpay
    normalpay = pay * hrs
    totalpay = normalpay + overtotal
    print("Your pay is", totalpay)

main()
