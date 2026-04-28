## cmpsc132 final project
##Shu Zhu
'''
3. Number Guessing Game (Single Player, Terminal-Based)

Description
A single player, terminal based number guessing game
where the computer generates a random number
and the player attempts to guess based on feedback.
After each guess, the program gives feedback
such as "Too High" or "Too Low"
until the correct number is guessed.
This is a simple but effective project
to practice logic building, loops, and input handling.

Requirements
. Random Number Generation:
    Game starts by a random number generation by the
    program (e.g., between 1 and 100)
. User Input:
    Player guesses the number
    (using the input() function
    and convert to int())
    User is allowed multiple attempts to guess the number
· Provide feedback:
    o "Too high": If the guess is greater than the number generated, it prompts the
    user to guess a lower number.
    o "Too low": If the guess is lower than the number generated, it prompts the
    user to guess a higher number.
    o "Correct!": If the guess matches, game displays "Congratulations!" and ends
    the game.
. Attempt Tracking:
    Program should keep track of the number of attempts
. End the game when the correct number is guessed

Implementation Details
. Use: random.randint(1, 100)
. Use a loop to continue until the correct guess
· Validate user input (ensure it is a number)
. Store and display the number of attempts

Suggested Enhancements (Optional)
. Difficulty levels (easy, medium, hard)
. Limit number of attempts
. Allow replay
'''
import random


##. Random Number Generation:
##    Game starts by a random number generation by the program (e.g., between 1 and 100)
def randomNum():
    return random.randint(1,100)

##. User Input:
##    Player guesses the number
##    (using the input() function
##    and convert to int())
##    User is allowed multiple attempts to guess the number
def userInput():
    guess = ""

    while not guess.isdigit():
        guess = input("Enter your guess: ")

        try:
            guess = int(guess.strip())
        except ValueError:
            print("Please enter a valid integer!")
        else:
            return guess

##· Provide feedback:
##    o "Too high": If the guess is greater than the number generated, it prompts the
##    user to guess a lower number.
##    o "Too low": If the guess is lower than the number generated, it prompts the
##    user to guess a higher number.
##    o "Correct!": If the guess matches, game displays "Congratulations!" and ends
##    the game.
def checkGuess(a, guess):
    if guess > a:
        return("Too high. Try to guess a lower number. ↘↘↘")
    elif guess < a:
        return("Too low. Try to guess a higher number. ↗↗↗")
    else:
        return("Correct!")


main
