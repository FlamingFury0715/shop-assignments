# naturalsum.py
# Phoenix Iserman 11/20/18
# Adds the first natural numbers up to the User's preference

n = 0

def main():
    loop = eval(input("what number do you want to go up to? "))
    n = 0
    for i in range(1, loop):
        n = n + i
    print(n)

main()
