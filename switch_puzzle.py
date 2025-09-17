import random

choice = [1, 2]

switch1 = random.randint(1, 2)
switch2 = random.randint(1, 2)
switch3 = random.randint(1, 2)

while True:
    choice1 = int(input("Choose to switch first switches or not: "))
    while choice1 not in choice:
        print("Wrong, please try again")
        choice1 = int(input("Choose to switch first switches or not: "))

    choice2 = int(input("Choose to switch second switches or not: "))
    while choice2 not in choice:
        print("Wrong, please try again")
        choice2 = int(input("Choose to switch second switches or not: "))

    choice3 = int(input("Choose to switch third switches or not: "))
    while choice3 not in choice:
        print("Wrong, please try again")
        choice3 = int(input("Choose to switch third switches or not: "))

    if switch1 == choice1 and switch2 != choice2 and switch3 != choice3 or switch2 == choice2 and switch1 != choice1 and switch3 != choice3 or switch3 == choice3 and switch1 != choice1 and switch2 != choice2:
        print("You got one correct")
    elif switch1 == choice1 and switch2 == choice2 and switch3 != choice3 or switch1 == choice1 and switch3 == choice3 and switch2 != choice2 or switch2 == choice2 and switch3 == choice3 and switch1 != choice1:
        print("You got two correct")
    elif switch1 == choice1 and switch2 == choice2 and switch3 == choice3:
        print("You got three correct")
    else:
        print("You got zero correct")

    if switch1 == choice1 and switch2 == choice2 and switch3 == choice3:
        print("Congratuations the light is on")
        break
    else:
        print("Failed, try again")
