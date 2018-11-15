# avg2.py
# Phoenix Iserman 11/15/18
# simple program to average two scores
# shows use of multi-input

def main():
    print("This program computes the average of three exam scores. ")

    score1, score2, score3 = eval(input("enter three scores, seperated by commas: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the score is: ", average)

main()
