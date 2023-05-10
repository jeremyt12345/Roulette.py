# Jeremy Thomas
#
# 4/16/23
#
# guessNumber.py
#
# Implement a number guessing game where a player will get up to seven
# chances to guess a mystery number in the range of 1 through 100.
#
# At the beginning of the game, the program will generate a random number
# in the range 1 through 100. It will then prompt the player to guess the
# number.
#
# If the guess is higher than the random number "Too high ..." will display
# If the guess is lower than the random number "Too low ..." will display
#
# The program will run for seven rounds.

# We need to import random numbers from our library because we will need random
# numbers generated to run the program upon user's guesses.
import random


# Let's define our function. Our function will run this program
# Within our "main" function we need to define our constant and variables
# These constants and variables are needed to run this desired program
def main():
    first = 1
    last = 100
    userGuess = 0
    roundNum = 0
    numGuesses = 0
    randomNumber = random.randrange(1,101)
# Define Variables. A (variable) is a storage container to hold data in python
    
# Define constant, a constant is a variable that has a value that
# cannot be changed.

    ROUNDS = 7
# Display Intro
    print('Guess the Mystery Number ...\n')
# Continues loop until correct number is guessed or goes seven rounds.
    while numGuesses < 7 and userGuess != randomNumber:
        roundNum += 1
        numGuesses += 1
        # Every time the user guesses incorrect the round will increase^
        # Display Game Round
        print ('Round', roundNum, 'of', ROUNDS, '\n'+
               '-------------')

        # Calls the function to validate the user's guess.
        userGuess = getGuess(first, last)
        # Calls the function to compare the user's guess to the number by passing parameters
        guessWin(userGuess, randomNumber)
        # Now we're going to see if the user would want to play again
        choice = input('Would you like to try again (y/n)?')
        # if user calls for main function
        if choice == 'y':
            main()

         # If anything else break the loop
        else:
             print('Goodbye')
        # Returns range of user's guess value.
def guessWin(guess,number):
    if guess < number:
        return print('--->', guess, 'is too low...')
    # Prints that guess is too low^
    elif guess > number:
        return print('--->', guess, 'is too high...')
    elif guess == number:
        return print('Congratulations ... You guessed the Mystery Number!')
    # If user doesnt get correct number display error
    else:
        return print('Error...Incorrect number. Try again.')
    # This last function getGuess defines the last function
def getGuess(first,last):
    guess = 0
    #Ask user for input
    guess = int(input('Enter your guess (1-100):'))
    #Enters loop again
    while first > guess or guess > last:
        print('Erroe...Incorrect number. Try again.')

        guess = int(input('Enter your guess (1-100):'))
    return guess
main()
    
        
     

    
        


    
