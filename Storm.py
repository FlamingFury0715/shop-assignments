# storm.py
# Phoenix Iserman 11/19/18
# measures distance away from lightning strike

def main():
    speed = 1100
    time = eval(input("how many seconds passed between the flash and the sound? "))
    distance = (time * speed) / 5280
    print("the strike was", distance, "miles away")
    input("press the <enter> button to quit")
    
main()
