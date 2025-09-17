import random

random = random.randint(1, 3)

if random == 1:
    computer_choice = "Rock"
elif random == 2:
    computer_choice = "Paper"
elif random == 3:
    computer_choice = "Scissors"

player_choice = int(input("Choose one (1. Rock, 2. Paper, 3. Scissors): "))

if player_choice == 1:
    player_choice = "Rock"
elif player_choice == 2:
    player_choice = "Paper"
elif player_choice == 3:
    player_choice = "Scissors"

print(f"Computer choose: {computer_choice}")

if computer_choice == player_choice:
    print("Tie")
elif player_choice == "Rock" and computer_choice == "Scissors" or player_choice == "Paper" and computer_choice == "Rock" or player_choice == "Scissors" and computer_choice == "Paper":
    print("Player win")
else:
    print("Computer win")
