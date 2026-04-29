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
. Difficulty levels (easy, medium, hard)v
. Limit number of attempts v
. Allow replay v
'''
import random


##. Random Number Generation:
##    Game starts by a random number generation by the program (e.g., between 1 and 100)
def randomNum(rangeUBd):
    return random.randint(1,rangeUBd)

##. User Input:
##    Player guesses the number
##    (using the input() function
##    and convert to int())
##    User is allowed multiple attempts to guess the number
def userInput():
    guess = ""
    validNum = False

    while not validNum:
        guess = input("Enter your number: ")
        guess = (guess.strip().lower())
        
        try:
            if guess == "exit":
                print("Exit Guessing...")#
                return
            
            guess = int(guess.strip())
            if guess>=1:
                return guess
            
            else:
                print("Please enter a valid integer!")
                
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

#move status check here for better adding dificult mode & attempt limitation
def statusChk(iniNum, attemptCount, status, guess, attUpperBd):

    while status != True:
        guess = userInput()

        if guess == "exit" :
            print("See you next time!")
            return
        
        status = feedback(iniNum, guess)
        attemptCount += 1

        if attemptCount == attUpperBd:
            status = True
            print(f"Challenge failed! You have reached the limit of attempts: {attUpperBd}\n"
                  +f"The corrct number is {iniNum}.\n"
                  +'-'*20)
            return
    
        if status:
            print(f"Your total number of guess is: {attemptCount}\n"+'-'*20)

#. Allow replay v
def anotherAttempt():
    anotherOrN = ''
    decision = False

    while not decision:
        anotherOrN = input("Do you want to play it again? ('Y'/'N')\n")
        anotherOrN = (anotherOrN.strip().lower())

        if anotherOrN == "n":
            decision = True
            print("See you next time!")
            return
            
        elif anotherOrN == "y":
            decision = True
            print("Got it! New round loading... \n"+'='*40)
            return main()

        else:
            print("Please enter a valid character!\n")


#. Limit number of attempts v
def limForAtt(mode):
    decision = False
    
    while not decision:
        setOrN = input(f"Wanna set a target for the highest number of attempts to challenge yourself?\n"
                   + "The number of attempts could be up to 100!\n"
                   + "'Y' for Yes"
                   + ' '*6
                   + "'N' for No\n")
        setOrN = (setOrN.strip().lower())

        if setOrN == "n":
            decision = True
            print("The number of attempts would be up to 100~\n")
            return 100
                
        elif setOrN == "y":
            #
            print("What's the limitation you wanna set?")
            atUpperBd = userInput()
            decision = True
            print(f"Sure! Your plan to guess the correct number within {atUpperBd} times.")
            return atUpperBd
            
        else:
            print("Please enter a valid character!\n")


#. Difficulty levels (easy, medium, hard)v
def setLv():
    decision = False
    while not decision:
        setOrN = input(f"Set the Difficulty levels to start: \n"
                   + "'1' for Easy: Guess a number from 1 to 10\n"
                   + "'2' for Medium: Guess a number from 1 to 100\n"
                   + "'3' for Hard: Guess a number from 1 to 1000 within at most 100 attempts!\n")
        setOrN = (setOrN.strip().lower())

        if setOrN == "1":
            decision = True
            print("Goal: Guess a number from 1 to 10! \n")
            return 10
        elif setOrN == "2":
            decision = True
            print("Goal: Guess a number from 1 to 100! \n")
            return 100  
        elif setOrN == "3":
            decision = True
            print("Goal: Guess a number from 1 to 1000! \n")
            return 1000

        else:
            print("Please enter a valid character!\n")
            

## ====================
def main():
    print ("Welcome to our Number Guessing Game!\n"
           +'-'*40
           + '\n'
           +"Tips: You can exit the game by entering 'Exit'\n"
           )
    mode = ""

    rangeUBd = setLv()
    attUpperBd = limForAtt(mode)

    print(f"Goal: Guess a number from 1 to {rangeUBd} within {attUpperBd} attemps!\n"
          + "==Are you ready? Let's go!==") 
    iniNum = randomNum(rangeUBd)
    print(iniNum) #for check purpose, TO BE DELETED after finishing the optionals!!!
    
    attemptCount = 0 #Attempt Tracking
    status = False
    guess = ''
    
    status = statusChk(iniNum, attemptCount, status, guess, attUpperBd)
            
    anotherAttempt()

if __name__ == "__main__":
    main()
