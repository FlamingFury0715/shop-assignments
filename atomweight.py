#atomweight.py
#Phoenix Iserman 11/19/18
#measures molecular weight of carbs

def main():
    H = 1.00794
    C = 12.0107
    O = 15.9994
    Hquan = eval(input("How many Hydrogen atoms are being measured? "))
    Cquan = eval(input("How many Carbon atoms are being measured? "))
    Oquan = eval(input("How many Oxygen atoms are being measured? "))
    carb = (H * Hquan) + (C * Cquan) + (O * Oquan)
    print("The carb you made weighs", carb)
    input("Press any button to exit")

main()
