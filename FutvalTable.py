#futval.py
#Phoenix Iserman 11/15/18
#computes investments
#carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the amount of time the investment will last: "))
    yeartot = 1
    print("Year    Value")
    print("=================")
    print("0      $", principal)
    for i in range (year) :
        principal = principal * (1 + apr)
        prinRound = round(principal, 2)
        print(yeartot, "     $", prinRound)
        yeartot += 1
    #print("The value in 10 years is: ", principal)

main()
