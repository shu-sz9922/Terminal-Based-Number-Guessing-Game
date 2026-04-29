##CMPSC 132 Final project
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
. Random Number Generation:v
    Game starts by a random number generation by the
    program (e.g., between 1 and 100)
. User Input:v
    Player guesses the number
    (using the input() function
    and convert to int())
    User is allowed multiple attempts to guess the number
· Provide feedback:v
    o "Too high": If the guess is greater than the number generated, it prompts the
    user to guess a lower number.
    o "Too low": If the guess is lower than the number generated, it prompts the
    user to guess a higher number.
    o "Correct!": If the guess matches, game displays "Congratulations!" and ends
    the game.
. Attempt Tracking:v
    Program should keep track of the number of attempts
. End the game when the correct number is guessed

Implementation Details
. Use: random.randint(1, 100)v
. Use a loop to continue until the correct guess v
· Validate user input (ensure it is a number) v
. Store and display the number of attempts v

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
        guess = input("Enter your guess from 1-100: ")
        guess = (guess.strip().lower())
        
        try:
            if guess == "exit":
                print("Exit Guessing...")#
                return guess
            guess = int(guess.strip())
            return guess
        except ValueError:
            print("Please enter a valid integer!")
        

##· Provide feedback:
##    o "Too high": If the guess is greater than the number generated, it prompts the
##    user to guess a lower number.
##    o "Too low": If the guess is lower than the number generated, it prompts the
##    user to guess a higher number.
##    o "Correct!": If the guess matches, game displays "Congratulations!" and ends
##    the game.
def feedback(iniNum, guess):
    if guess > iniNum:
        print("Too high. Try to guess a lower number. ↘↘↘")
        return False
    elif guess < iniNum:
        print("Too low. Try to guess a higher number. ↗↗↗")
        return False
    else:
        print("Correct!")
        return True


def main():
    iniNum = randomNum()
    #for check purpose
    print(iniNum)
    
    attemptCount = 0 #Attempt Tracking
    status = False
    guess = 0
    
    while status != True:
        guess = userInput()
        if guess == "exit" :
            print("See you next time!")
            return
        
        status = feedback(iniNum, guess)
        attemptCount += 1
            
        if status:
            print(f"Your total number of guess is: {attemptCount}")
            
    

if __name__ == "__main__":
    main()
