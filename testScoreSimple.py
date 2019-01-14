# testScoreSimple.py
# Phoenix Iserman
# 12/13/2018
# scores tests with a max score of 5

def main():
    var = eval(input("How many answers were correct on the test? "))
    if var == 5:
        letter = "A"
    if var == 4:
        letter = "B"
    if var == 3:
        letter = "C"
    if var == 2:
        letter = "D"
    if var <= 1:
        letter = "F"
    if var >= 6:
        letter = "-Hey! That wasn't an option!"
    print("The score of this test is {0}".format(letter))


main()
