# caesarloop.py
# Phoenix Iserman
# 1/2/19
# encrypts input through caesar cypher. will loop around if it goes beyond Z.

def main():
    key = eval(input("input your key. if it's positive, it will encode, but it it's negative, it will decode."))
    phrase = input("what is the phrase you want to run through the cipher? ")
    var = 0
    for acro in list(phrase):
        x = (ord(phrase[var]) + key)
        print(chr(x))
        var += 1



main()
