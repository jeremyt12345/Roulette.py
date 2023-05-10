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
# Define main function.
def main():
    # Define Constant.
    ROUNDS = 7
    # Define Variables. A variable is a storage container to hold data in python
    # 
    first = 1
    last = 100
    userGuess = 0
    roundNum = 0
    numGuesses = 0
    randomNumber = random.randrange(1,101)
    choice = 'y'
    # Intro.
    print('Guess the Mystery Number ...\n')
    # Continues loop until 7 rounds have passed
    while numGuesses < 7 and userGuess != randomNumber:
        # Adds to the count of rounds and guesses.
        roundNum += 1
        numGuesses += 1
        # Displays game round.
        print('Round', roundNum, 'of', ROUNDS,'\n'+
            '-------------')
        # Calls the function to validate the user's guess.
        userGuess = getGuess(first, last)
        # Calls the function to compare the user's guess to number by passing parameters.
        guessWin(userGuess, randomNumber)
    # Asks the user if they would like to play again.
    choice = input('Would you like you try again (y/n)?')
    # If y then call main function.
    if choice == 'y':
        main()
    # If anything else, break.
    else:
        print('Goodbye.')
# Returns range of user's guess value.        
def guessWin(guess, number):
        # Prints that guess is too low if too low.
        if guess < number:
            return print('--->', guess, 'is too low...')
        # Prints that guess is too high if too high.
        elif guess > number:
            return print('--->', guess, 'is too high...')
        # Congratulates user if correct.
        elif guess == number:
            return print('Congratulations ... You guessed the Mystery Number!')
        # If anything else is entered, respond with error.
        else:
            return print('Error...Incorrect number. Try again.')
# Defines the get guess validation function.        
def getGuess(first, last):
        # Defines functions variables.
        guess = 0
        # Asks for user's input.
        guess = int(input('Enter your guess (1-100):'))
        # Enters loop of validation until true.
        while first > guess or guess > last:
            # If false, respond with error and continue.
            print('Error...Incorrect number. Try again.')
                
            guess = int(input('Enter your guess (1-100):'))
            # If true, break and return guess.
        return guess
main()
