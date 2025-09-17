import random
bigger = False
finalnumber = 0
for i in range(0,101):
    number = random.randint(0,100)
    if number > 50:
        bigger = True
    else:
        bigger = False
    if bigger == True:
        finalnumber = finalnumber + number
    print("Current number:", number)
    print(finalnumber)