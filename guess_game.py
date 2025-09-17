import random
import time

random_number = random.randint(0, 500)
attempt = 0

while True:
    your_guess = int(input("Take a guess: "))
    print("")
    if your_guess > random_number:
        print("⬇️  \033[31mLower\033[0m")
        attempt += 1
        print(f"You have guess {attempt} time(s)")
    elif your_guess < random_number:
        print("⬆️  \033[31mHigher\033[0m")
        attempt += 1
        print(f"You have guess {attempt} time(s)")
    else:
        print("🎉 Congratulation you have found out the correct number")
        break
    if attempt == 10:
        print("Out of guesses")
        break
    time.sleep(2.5)
    print("")
