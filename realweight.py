# Jeremy Thomas

# 4/9/2023

# Intro to Programming

# weight.py

# Define main function
def main():
    option = 0
    month = 0
    weight = 0
    #Title
    print('500 Less a day Makes the Weight Go Away ...')
    print()
# My goal is to display 3 different options for the user
# Each Option is a loop, each loop will display three
# different menus
    while option != 3:
        
# Above^ is stating that the prompt/loop will exit when/if the user enters 3.
    
        option = int(input('Choose one of the following options:\n'+
                   '    1. Display "10 ways to cut 500 calories" guideline.\n'+
                   '    2. Generate next semester expected weight table.\n'+
                   '    3. Quit.\n'+
                   'Option: '))
        print()
        

# Above^ is giving the user to input the option and display their choice.

        if option == 1:
            print('Try these 10 ways to cut 500 calroies every day.\n'+
                      '    * Swap you snack.\n'+
                      '    * Cut one high-calorie treat.\n'+
                      '    * Do NOT drink your calories.\n'+
                      '    * Make low calorie substitutions.\n'+
                      '    * Ask for a doggie bag.\n'+
                      '    * Just say no "no" to fried food\n'+
                      '    * Build a thinner pizza.\n'+
                      '    * Use a smaller plate.\n'+
                      '    * Avoid alcohol.\n'+
                      'Source: US National Library of Medicine.')
            print()
# ^These are the options user sees after selecting "1."
        elif option == 2:
                weight = int(input('Please enter starting weight in pounds (>=100): '))
# If the user selects to "2" a weight over 100 pounds will be prompted to enter
                if weight >= 100:

                    print('-----------------\n'+
                          'Month   Weight\n'+
                          '-----------------')
                    
                    for month in range(1,7):
                        PROJWEIGHT = weight - (month * 4)
                        print(month, '       ', PROJWEIGHT, 'lb.')
 # ^Now the user will see their weight every month for six months subtracted by 4 pounds                   


                elif weight < 100:
# ^Here we have a possibility the user enter a weight less than 100
                    while weight < 100:
# ^ A loop is created for this scenario.                        

                        print('Error ... Invalid weight. Try Again')

                        weight = int(input('Please enter starting weight in pounds (>=100): '))
# After that error message the user again will be able to choose to enter a weight
# above 100 pounds again                        
                        if weight >= 100:
                            for month in range(1,7):

                                PROJWEIGHT = weight - (month * 4)

                                print(month, '    ', PROJWEIGHT)
 # Breaks loop in case of error.
                        else:
                            break
                                

                         

        elif option == 3:

             print('Good Bye ...')

             break

        else:
             print('That option is not valid.')
main()             


            
