import random
import os


def generateRrandom():
    return random.randint(1, 10)


def restartGame():
    userInput = input("Do you want to restart ? [Y/n] ")
    if userInput.lower() == "y":
        startGame()
    else:
        print("Goodbye !")


def startGame():
    guesses += 1
    os.system('cls')
    numberToFind = generateRrandom()

    while True:
        userGuess = input("Make a guess: ")

        if userGuess.isdigit():
            userGuess = int(userGuess)
        else:
            print("Please type a number")
            continue

        if userGuess == numberToFind:
            print("You got it in " + str(guesses) + " !")
            restartGame()
            break
        elif userGuess > numberToFind:
            print("You were above the number !")
        else:
            print("You were below the number !")


startGame()
