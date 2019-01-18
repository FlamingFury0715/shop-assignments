# dsDayNum.py
# 1/18/19
# Phoenix Iserman
# Tells what number day of the year the given date is


def main():
    month, day, year = input("What date (MM/DD/YYYY) do you wish to check? ").split("/")
    if (int(year) % 4) == 0:
        if (int(year) % 100) == 0:
            if (int(year) % 400) == 0:
                collateral = 1
            else:
                collateral = 0
        else:
            collateral = 1
    else:
        collateral = 0
    daynum = 31 * (int(month) - 1) + int(day) + collateral
    if int(month) >= 2:
        collateral2 = (4 * (int(month)) + 23) // 10
        daynum -= collateral2
    print("The given date is the", str(daynum), "day of the year")


main()
