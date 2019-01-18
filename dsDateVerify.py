# dsDateVerify.py
# 1/18/19
# Phoenix Iserman
# validates an entered date

def main():
    month, day, year = input("Please enter a date in the format MM/DD/YYYY: ").split("/")
    error = "Invalid date"
    if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 9 or int(month) == 11:
        if int(day) > 31:
            print(error)
    if int(month) == 4 or int(month) == 6 or int(month) == 8 or int(month) == 10 or int(month) == 12:
        if int(day) > 30:
            print(error)
    if int(month) ==2:
        if int(day) > 28:
            print(error)
    if int(month) > 12:
        print(error)
    else:
        print("The date is valid.")
    
main()
