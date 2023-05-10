# jeremy thomas
# roulette.py
# this is a roulette that runs and prompts the user
# to enter a pocket number and goes to that color within that set
def main():
    print()
#^ this "print()" simply just allows
#  me to be able to have an extra space for formatting purposes

    print('Roulette Wheel Colors App ...')
    print()



# I now want to create a variable which i'll name "user_pocket_number"
# "user_pocket_number" needs to be input by the user so I'm going to include my "input"
# but dont forget because I'm asking the user to input an integer Im also going to add "int"
# when this happens we want it to look like "int(input("...."))
# my prompt "Please enter pocket number (0-36): " will be inside my "int(input("..."))
user_pocket_number = int(input("please enter a pocket number: "))

print()

if user_pocket_number < 0 or user_pocket_number > 36:
    print("      Error... Invalid pocket. Try Again")

 # ^ To keep the game flowing and within the boundaries the code I wrote above has 0-36
 # ^ as the only possible number, all else will present a error message.
elif user_pocket_number == 0:
    print("The color of the pocket is green")



 # Just like a real roulette board "0" is a green pocket so I wrote a statement
 # that follows that, if the user inputs "0" we receive "the color of the pocekt is green"
elif (((user_pocket_number >=1 and user_pocket_number <=10 or
      user_pocket_number >=19 and user_pocket_number <=28) and
      not user_pocket_number % 2 == 0) or
# ^I had some trouble understanding this but bare with me
# We want for different pockets to be red or black
# But we also want the variation of red and black to be different
# For example, in the range 1-10 and 19-28
# In those ranges we want the odd number to be red and the even to be black
# In the range 11-18 and 19-28 we want the opposite, we want even to be red and odd to be black
# Now how do we do that? "%" means remainder, when you divide an even number by 2 you get no remainder
# 4/2 = 2 (no remainder), but 3/2 = 1.5 ".5" is our remainder here
# We have a remainder because 3 is odd
# So above in my code I wrote that from 1-10 and 19-28 every number that does NOT
# have a 0 as its remainder (all odd numbers) will be red. And I stated I want the
# opposite in range 11-18 and 29-36.
# Its important to understand this because this here is the engine of the gam      


       ((user_pocket_number >=11 and user_pocket_number <=18 or
        user_pocket_number >=29 and user_pocket_number <=36 ) and
        user_pocket_number % 2 == 0)):
       
         print("The color of the pocket is red")
else:
        print("The color of the pocket is black")
