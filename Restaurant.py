#Jeremy Thomas

#Intro to Programming

#Restaurant.py

#3/27/23

#This is the restaurant bill generator.

#the user is prompted to input the cost of food and drinks

#then the generator will produce an output (bill) that calculates the total of food and drinks, tax after total and tip.

def main():
 print("Restaurant Bill Generator ...")
 print()
# Get input from user
 food = float(input("Please enter cost of food: $"))
 drinks = float(input("Please enter cost of drink: $"))
 print()
 
# This is what the customer will see after meal

 print("Restaurant Bill")
 print("-----------------------------------------------")
 print()

# Cost of meal=food and drinks
 meal= (food + drinks)
 print(" Cost of Meal:      $              ", format(meal, '.2f'))

# Configure tax amount
 tax = 7.5/100 * (food + drinks)
 print(" Tax Amount:        $               ", format(tax, '.2f'))



# Configure tip amount
 tip = 18/100 * (meal+ tax)
 print(" Tip Amount:        $               ", format(tip, '.2f'))

 print("                ------------------------------")

# Everything added up = total

 total = (tip+ tax + drinks + food)
 print(" Total:             $              ",format(total, '.2f'))

main()
