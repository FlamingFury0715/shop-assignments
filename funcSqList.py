# funcSqList.py
# 1/16/19
# Phoenix Iserman
# squares every number in a list

def squareEach():
    entry = input("Input the numbers you wish to use, seperated by spaces: ")
    numlist = entry.split()
    sqList = []
    for num in numlist:
        newnum = int(num) ** 2
        sqList.append(newnum)
    print(sqList)

squareEach()
