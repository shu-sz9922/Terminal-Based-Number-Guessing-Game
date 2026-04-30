# CMPSC 132 Project Code: A Terminal-Based Number-guessing Game

## Introduction

This project implements a single-player number-guessing game in Python. The objective is for the player to guess a randomly generated number using system feedback. The project focuses on practicing core programming concepts such as conditionals, logic building, loops, functions, and user input validation.


## Program Design
The program is modular and organized into multiple functions. Each function is responsible for a
specific task. This design avoids the use of `break` statements by using control variables to manage loop execution. This ensures clearer logic flow and better maintainability.

- `randomNum()`: Generates a random number within a given range.
- `userInput()`: Handles user input and validates it.
- `feedback()`: Provides hints based on the user's guess.
- `statusChk()`: Controls the main game loop and tracks attempts.
- `setLv()`: Allows the user to select the difficulty level.
- `limForAtt()`: Sets a limit on the number of attempts.
- `anotherAttempt()`: Prompts the user to replay the game.
- `main()`: Coordinates the entire game execution.


## Implementation Details

The game begins by prompting the user to select a difficulty level, which determines the range of the random number.
The user can optionally set a maximum number of attempts.

The system then generates a random number using Python's `random.randint()` function. A loop continues until the player either guesses correctly, reaches the attempt limit, or exits the game. 

Input validation ensures that the user provides valid numeric input.


## Features and Enhancements

In addition to the basic requirements, several enhancements were implemented.
The game includes multiple difficulty levels, allowing the player to choose between easy, medium, and hard modes. A customizable attempt limit adds an extra challenge.
The program also supports replay functionality, enabling the user to play multiple rounds without restarting the program.

These features improve user experience and demonstrate advanced logic design.


## Challenges and Solutions

One challenge was implementing loop control without using break statements. This was solved by introducing control variables that determine when the loop should terminate. 
Another challenge was handling user input robustly. This was addressed using try-except blocks to catch invalid input and prompt the user again.


## Conclusion

This project successfully implement a terminal-based number-guessing game.
It reinforces key programming concepts such as modular design, input validation, and loop control. 
The enhancements added to the base game make it more interactive and engaging. 
Overall, the project serves as a great example of applying fundamental programming techniques to build a complete application.
