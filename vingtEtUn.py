#Jeremy thomas
# 5/6/23
import random

# import random will pull in numbers that will help with game because we will be rolling dice
def display_rules():
    print("Vingt-et-un is a dice game (known as Blackjack in the USA), where a player competes against the computer (house).")
    print("The goal of the game is to score 21 points, or as near as possible without going over.")
    print("The two players take turns throwing two dies as many times as desired and adding up the numbers thrown on each round.")
    print("A player who totals over 21 is bust and loses the game.")
    print("The player whose total is nearest 21, after each player has had a turn, wins the game.")
    print("In the case of an equality high total, the game is tied.")
    print("The game is over at the end of a round when:")
    print("- One or both players are bust.")
    print("- Both players choose to stay.")
    print("Notes:")
    print("- Once a player totals 14 or more, one of the dies is discarded for the consecutive turns.")
    print("- The house must throw the dice until the total is 17 or higher. At 17 or higher, the house must stay.")
    print()
# The rules will be there for the user if they want to see them after selcting option #1
def roll_dice(num_dice):
    return sum([random.randint(1, 6) for _ in range(num_dice)])
# This return sum() is for the dice once rolled
def play_vingt_et_un(player_name):
    print(f"Welcome to Vingt-et-un, {player_name}!")
    # The user is asked for their name
    while True:
        print("Choose an option:")
        print("1. See the Rules.")
        print("2. Play Vingt-et-un.")
        print("3. Quit.")
        choice = input("> ")
        if choice == "1":
            display_rules()
            # Here is where the game starts, because nobody has rolled each starts with 0
        elif choice == "2":
            print("Let's play!")
            player_total = 0
            house_total = 0
            while True:
                print(f"{player_name}, your current total is {player_total}.")
                print(f"The house's current total is {house_total}.")
                # The program will run after the first roll to tell us our total along with the house and what they rolled
                if house_total >= 17:
                    print("The house stays.")
                    break
                # After a few rolls if the house lands at 17 we want the house to stop, which is why we have the "break" because that breaks the loop
                else:
                    house_roll = roll_dice(2 if house_total < 14 else 1)
                    house_total += house_roll
                    # If not the house rolls again if their total is under 14 and once if they are from 14-16
                    print(f"The house rolls {house_roll}.")
                while True:
                    choice = input("Do you want to (R)oll or (S)tay? ").lower()
                    if choice == "r":
                        player_roll = roll_dice(2 if player_total < 14 else 1)
                        player_total += player_roll
                        print(f"You roll {player_roll}. Your current total is {player_total}.")
                        # the game gives the same option as the house gets
                        if player_total > 21:
                            print("You bust!")
                            break
                        # This will end the game POSSIBLY
                    elif choice == "s":
                        print("You stay.")
                        break
                    # if you want the house to keep rolling
                    else:
                        print("Invalid choice. Please enter R or S.")
                if player_total > 21:
                    break
            if player_total > 21:
                print(f"Sorry, {player_name}, you lose!")
                # if you kept rolling and rolled higher than 21, you lose
            elif house_total > 21:
                print(f"Congratulations, {player_name}, you win!")
                # the opposite here, if the house messes up you win
            elif player_total > house_total:
                print(f"Congratulations, {player_name}, you win!")
            elif player_total < house_total:
                print(f"Sorry, {player_name}, you lose!")
            else:
                print("It's a tie!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

play_vingt_et_un(input("What is your name"))

