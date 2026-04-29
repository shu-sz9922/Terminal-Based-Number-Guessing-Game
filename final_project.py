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
    while True:
        guess = input("Enter your number: ").strip().lower()

        if guess == "exit":
            print("Exit Guessing...")
            return "exit"
    
        try:
            guess = int(guess)
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
def statusChk(iniNum, attUpperBd):
    attemptCount = 0
    while True:
        guess = userInput()

        #C1: exit
        if guess == "exit" :
            return "exit"

        else:
            attemptCount += 1
            correct  = feedback(iniNum, guess)

            #2: Correct guess
            if correct:
                print(f"Your total number of guess(es) is: {attemptCount}\n"+'='*40)
                gameOver = True
                return

            #3: Limit reach
            elif attemptCount >= attUpperBd:
                print(f"Challenge failed! You have reached the limit of attempts: {attUpperBd}\n"
                      +f"The correct number is {iniNum}.\n"
                      +'-'*20)
                return
      

#. Allow replay v
def anotherAttempt():#return gameOver val
    while True:
        choice = input("Do you want to play it again? ('Y'/'N')\n").strip().lower()

        #C1: exit
        if choice == "exit" :
            return "exit"
        
        if choice == "y":
            print("Got it! Loading a new round ... \n"+'='*40)
            return False
        
        elif choice == "n":
            print("See you next time!")
            return True

        else:
            print("Please enter a valid character!\n")


#. Limit number of attempts v
def limForAtt():
    while True:
        setOrN = input(f"Wanna set a target for the highest number of attempts to challenge yourself?\n"
                   + "The number of attempts could be up to 100!\n"
                   + "'Y' for Yes"
                   + ' '*6
                   + "'N' for No\n"
                       ).strip().lower()

        #C1: exit
        if setOrN == "exit" :
            return "exit"

        else:
            if setOrN == "n":
                decision = True
                print("Attempts limit set to 100.")
                return 100
                    
            elif setOrN == "y":
                #print("Enter attempt limit:")
                atUpperBd = userInput()

                #NEED exitChk() !!!
                if atUpperBd == "exit":
                    return "exit"

                
                print(f"Sure! Your goal is to guess within {atUpperBd} times.")
                return atUpperBd
            
            else:
                print("Please enter a valid character!\n")


#. Difficulty levels (easy, medium, hard)v
def setLv():
    while True:
        setOrN = input(f"Set difficulty to start: \n"
                   + "'1' for Easy: Guess a number from 1 to 10\n"
                   + "'2' for Medium: Guess a number from 1 to 100\n"
                   + "'3' for Hard: Guess a number from 1 to 1000!\n"
                       ).strip().lower()

        #C1 exit
        if setOrN == "exit" :
            return "exit"

        else:  
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


#check for exit signal and print ending
def exitChk(val):
    if val == "exit":
        print("See you next time!")
        return True
    return False


## ====================
def main():
    gameOver = False

    while not gameOver:
        print ("Welcome to our Number Guessing Game!\n"
               +"Tips: You can exit the game by entering 'Exit'\n"
               +'-'*40)
        
        rangeUBd = setLv()
        if exitChk(rangeUBd):
            return None
            
        attUpperBd = limForAtt()
        if exitChk(attUpperBd):
            return None

        print(f"Goal: Guess a number from 1 to {rangeUBd} within {attUpperBd} attempts!\n"
              + "Are you ready? Let's go!\n"
              +'-'*40) 

        iniNum = randomNum(rangeUBd)
        #print(iniNum) #for check purpose, TO BE DELETED after finishing the optionals!!!
        
        status = statusChk(iniNum, attUpperBd)
        if exitChk(status):
            return None
                
        gameOver = anotherAttempt()
        if exitChk(gameOver):
            return None
        

if __name__ == "__main__":
    main()
