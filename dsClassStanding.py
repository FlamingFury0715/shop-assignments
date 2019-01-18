# dsClassStanding.py
# 1/17/19
# Phoenix Iserman
# Calculates what class a student is in based off of the number of
# credits that they have

def main():
    creds = eval(input("How many credits do you currently have? "))
    if creds >= 0:
        studclass = "Freshman"
        if creds >= 7:
            studclass = "Sophomore"
            if creds >= 16:
                studclass = "Junior"
                if creds >= 26:
                    studclass = "Senior"
    print("You are a", studclass)


main()
