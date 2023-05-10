# jeremy thomas
# Life_Cycle.py
# Just playing around with "if" "else" and "elif" statements
# This morbid game will allow the user to enter their age,
# sex, height, weight, fitness level, average diet
# possible vices (smoking, drinking,)

# and calculate a guess...., because no one truly knows, of how long they may live


def main():
    print('Welcome To The Life Cycle Game...')
    print()
    print('My name is X3 ZEN and I have observed enough living beings to guess how long you might live')
    print()
    print('You look like a human from SOL III, a place that contains 78.08% nitrogen, 20.95% oxygen, 0.93% argon, 0.04% carbon dioxide, and small amounts of other gases.')
    print()
    print('But others call it Earth')
    print()
    print('Please dont ask me how I learned to speak this langauge it is a very violent story.')
    print()
    print('I dont want to waste your time and I have a hot date with a being from Uranus so lets make this quick')
    print()
    print('Lets start')
    print()



    AGE = int(input("So how many times cycles have you spun around on Earth?: "))

    if AGE >= 50 :
        print()
        print('You are ripe, you should have more time depending on my next questions')
    else:
        print()
        print('On average you have many moons left in your life cycle depending on my next questions')
        print()

    

    Sex = (input('On your day of birth were you given a female, male, both or other title: '))
    print()
    print('Hmmm, turn around... yea that makes sense')
    print()
    print()

    Height =(input(" How tall are you ,please tell me in words only?EX. five foot ____  "))
    print()
    print('Intresting you seem to be bigger than my last meal....I mean last friend!')
    print()

    Fitness_level = int(input("How many days per week do you work out?: "))
    if Fitness_level >= 3:
        print()
        print('Mmmmm nice and healthy, just how I like it')
        print()

    else:
         print('Thats not very promising, try a minimum of 3 days for healthy organs, brains, and dinner...uhhh I mean body')
         print()

    DIET = int(input('How many times per day do you eat plants: ?'))
    if DIET >= 3:
        print()
        print("You must be very tender")
    else:
        print()
        print("What a shame")

    SMOKE = input("Do you smoke?: ")
    if SMOKE == "Yes":
        print()
        print("Killer habit")
    elif (SMOKE != "Yes" or "yes"):
        print()
        print("Intersante")

    DRINK = input("Last question , do you drink more than 5x/week ??: ")
    if DRINK == "Yes":
         print()
         print('I know a guy that can help with that')
    elif (DRINK != "Yes" or "yes"):
          print()
          print('Keep it that way')
          print()

    if (AGE < 50, Fitness_level >= 3, DIET >= 3, SMOKE != "Yes" or "yes", DRINK != "Yes" or "yes"):
        print()
        print("You added up to my requirements, therefore SHORT LIFE FOR YOU! GET IN MY BELLY!")

    else:
        print()
        print("You will live a shorter than average life, but longer than today because I choose not to eat you. Carry on!")
    
    

    

    
    

        

main()

