# dsSpeedLimit
# 1/17/19
# Phoenix Iserman
# calculates if someone was over the speed limit

def main():
    limit = eval(input("What is the speed limit? "))
    carspeed = eval(input("How fast was the violator going? "))
    speeddiff = carspeed - limit
    bonus = 0
    if carspeed < limit:
        print("The 'violator' was not speeding.")
    else:
        initial = 50
        cumulative = 5 * speeddiff
        if carspeed > 90:
            bonus = 200
        totalfine = initial + cumulative + bonus
        print("Your fine is", totalfine)

main()
