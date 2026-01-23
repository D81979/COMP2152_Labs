# Solution for the Week 02 Lab
import random

choice = ["Rock", "Paper", "Scissor"]

playerChoice = input("Enter a number between 1 to 3 for the following choices: 1-Rock, 2-Paper, 3-Scissors: ")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be between 1 and 3!")
else:
    # Develop the gae logic using if/elif/else
    computerChoice = random.randint(1, 3)

    if playerChoice == computerChoice:
        print("It's tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissor - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beat Rock - You win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissor beats Paper - You win!")
    else:
        print("You lose!")