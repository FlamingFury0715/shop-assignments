#futval.py
#Phoenix Iserman 11/15/18
#computes investments
#carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    yr = eval(input("Enter the number of years you want to invest for: "))
    for i in range (10):
        principal = principal * (1 + apr)
    print("The value in ", yr, "years is: ", principal)

main()
