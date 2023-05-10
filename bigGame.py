def main():
    print("The Madlib Game...")
    print()
    print("Enter the following words:")
    # get input from user
    pnoun1 = input("Plural Noun: ")
    fname = input("Person's First Name: ")
    noun1 = input("Noun: ")
    lname = input("Person's Last Name: ")
    pnoun2 = input("Plural Noun: ")
    place1 = input("Place: ")
    pnoun3 = input("Plural Noun: ")
    place2 = input("Place: ")
    pnoun4 = input("Plural Noun: ")
    noun2 = input("Noun: ")
    adjective1 = input("Adjective: ")
    adjective2 = input("Adjective: ")
    verb = input("Verb: ")
    adjective3 = input('Adjective: ')
    print()
#  Displays the message "The Big Game !!!"
    print('\nThe Big Game !!!\n')
    print()
#   Displays the message "Hello there, pnoun!"
    print("Hello there, sports " +  pnoun1 + " !")
    print("This is " + fname + " , talking to you from the press " + noun1 )
    print("in " + lname + " stadium, where 57,000 cheering " + pnoun2 )
    print("have gathered to watch (the) " + place1 , pnoun3 )
    print("take on (the) " + place2 , pnoun4 + " .")
    print("Even though the " + noun2 + " is shining, it's a/an " + adjective1)
    print("cold day with the temperature in the " + adjective2 + " 20s.")
    print("We'll be back for the opening " + verb + " -off after a few words")
    print("from our " + adjective3 + " sponsor. ")
          
main()  # then call to main function

#  Jeremy Thomas
#  MadLib Game
#  bigGame.py
# Date: 3/26/23
# This program prompts the user to "enter the following words" and takes the input (Noun, Verb, Place, Adjective, Person's First and Last Name)
# and processes these words to produce the output and display the Madlib Game story through the main function.
# The output is the Madlib story and it is created by the input from the user. 
