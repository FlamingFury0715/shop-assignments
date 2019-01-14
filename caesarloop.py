# caesarloop.py
# Phoenix Iserman
# 1/2/19
# encrypts input through caesar cypher. will loop around if it goes beyond Z.
 
def main():
    key = eval(input("input your key. if it's positive, it will encode, but it it's negative, it will decode."))
    phrase = input("what is the phrase you want to run through the cipher? enter in all lowercase: ")
    var = 0
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for acro in list(phrase):
        x = ((ord(phrase[var]) + key) - 95)
        var2 = alpha[x]
        print(var2)
        var += 1



main()
