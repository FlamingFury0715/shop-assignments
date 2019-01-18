# dsLeapYear.py
# 1/18/19
# Phoenix Iserman
# Detects if a year is a leap year

def main():
    year = eval(input("What year do you wish to check? "))
    if (year % 4) == 0:
        if (year % 100) == 0:
           if (year % 400) == 0:
               print(year, "is a leap year")
           else:
               print(year, "is not a leap year")
        else:
           print(year, "is a leap year")
    else:
       print(year, "is not a leap year")

main()
