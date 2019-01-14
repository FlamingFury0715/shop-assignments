# Acronym.py
# Phoenix Iserman
# 12/14/18
# creates acronyms from the given phrases

def main():
    phrase = input("What is the phrase that you want to convert? ").split(" ")
    var = 0
    for acro in phrase:
        print(phrase[var][0].upper())
        var = var + 1
    


main()
