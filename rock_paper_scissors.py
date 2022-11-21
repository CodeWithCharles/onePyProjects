import random

userWins = 0
computerWins = 0
options = ["rock", "paper", "scissors"]

while True:
    userInput = input("Type Rock/Paper/Scissors [Q to quit]").lower()
    if userInput == "q":
        break

    if userInput not in options:
        continue

    computerPick = options[random.randint(0, 2)]
    print("Computer picked", computerPick + ".")

    if userInput == "rock" and computerPick == "scissors":
        print("You won !")
        userWins += 1

    elif userInput == "paper" and computerPick == "rock":
        print("You won !")
        userWins += 1

    elif userInput == "scissors" and computerPick == "paper":
        print("You won !")
        userWins += 1

    elif userInput == computerPick:
        print("Draw !")

    else:
        print("You lost !")
        computerWins += 1

print("You won", userWins, "times.")
print("The computer won", computerWins, "times.")
print("Goodbye !")
