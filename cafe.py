#Cafe.py
#Phoenix Iserman 11/20/18
#calculates price of a coffee shop order

def main():
    base = 10.50 #cost per pound of coffee (plus shipping)
    ship = 0.86 #ship cost per pound
    shipfix = 1.50 #fixed amount to pay for shipping
    order = eval(input("How many pounds of coffee do you want shipped? "))
    totalship = ((ship * order) + (base * order)) + shipfix
    print("The total price is $" + str(totalship))

main()
