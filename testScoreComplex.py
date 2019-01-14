# testScoreComplex.py
# Phoenix Iserman
# 12/13/2018
# scores tests with a range of 100-0.
# This script is an altered form of testScoreSimple.py

def main():
    var = eval(input("What was the number score on the test? "))
    if var >= 101:
        letter = "-Hey! That wasn't a possible score!"
    else:
        if var >= 90:
            letter = "A"
        else:
            if var >= 80:
                letter = "B"
            else:
                if var >= 70:
                    letter = "C"
                else:
                    if var >= 60:
                        letter = "D"
                    else:
                        if var <= 59:
                            letter = "F"
    print("The score of this test is {0}".format(letter))


main()
