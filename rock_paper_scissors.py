import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/paper/scissor or to quit: ").lower()
    options = ["rock", "paper", "scissor"]
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_picked = options[random_number]
    print("Computer picked", computer_picked + ".")
    if user_input == "rock" and computer_picked == "scissor":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_picked == " rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissor" and computer_picked == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_picked == "rock":
        print("You got the same!")

    elif user_input == "paper" and computer_picked == "paper":
        print("You got the same!")

    elif user_input == "scissor" and computer_picked == "scissor":
        print("You got the same!")

    else:
        print("You lost!")
        computer_wins += 1

print("You got", user_wins, "times.")
print("Computer got", computer_wins, "times.")
print("Goodbye.")
