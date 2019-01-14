# WordCountAdvanced.py
# Phoenix Iserman
# 1/3/19
# counts the amount of lines, words, and characters in a phrase


def main():
    usrinput = input("Please name the file (this is case sensitive!) you wish to get acount for: ")
    fileopen = open(usrinput, "r")
    doc = fileopen.read()
    charcount = 0
    space = " "
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,/?:;!@#$%^&*()1234567890-=_+"
    #character counter
    for char in chars:
        count = doc.count(char)
        charcount += count
    #word counter
    for char in space:
        wordcount = doc.count(space)
    #line counter
    linecount = sum(1 for line in open(usrinput))
    print("Words:", wordcount + 1)
    print("Characters:", charcount)
    print("Lines:", linecount)
    



main()
