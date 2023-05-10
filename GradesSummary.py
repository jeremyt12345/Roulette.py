import random
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4


def deal(deck):
    hand_user = []
    for i in range(2):
            random.shuffle(deck)
            card = deck.pop()
     
            if card == 11:card = "Jack"
            if card == 12:card = "Queen"
            if card == 13:card = "King"
            if card == 14:card = "Ace"
            hand_user.append(card)

    return hand_user
def play_again():

    ask_again = input("Play again? (Y/N) : ").lower()
    if ask_again == "y":
            dealer_hand = []
            player_hand = []
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
            game()

    else:
            print("Okay,Bye!")
            exit()
def total_in_hand(hand):
    total_in_hand = 0
    for card in hand:
            if card == "Jack" or card == "Queen" or card == "King":
                total_in_hand+= 10
            elif card == "Ace":
                if total_in_hand >= 11: total_in_hand+= 1
                else: total_in_hand+= 11
            else: total_in_hand += card
    return total_in_hand

def hit(hand):
        card = deck.pop()
        if card == 11:card = "Jack"
        if card == 12:card = "Queen"
        if card == 13:card = "King"
        if card == 14:card = "Ace"
        hand.append(card)
        return hand

def print_results(dealer_hand, player_hand):
        print("\n\nThe dealer has a " + str(dealer_hand) + " for a Total of " + str(total_in_hand(dealer_hand)))
        print("You have a " + str(player_hand) + " for a Total of " + str(total_in_hand(player_hand)))


def blackjack(dealer_hand, player_hand):
        if total_in_hand(player_hand) == 21:
                print_results(dealer_hand, player_hand)
                print ("\nCongratulations! Got a Blackjack!\n")
                play_again()
        elif total_in_hand(dealer_hand) == 21:
                print_results(dealer_hand, player_hand)         
                print ("\nLose. The dealer got a blackjack.\n")
                play_again()

def score(dealer_hand, player_hand):
    if total_in_hand(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! It is a Blackjack!\n")
    elif total_in_hand(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)         
        print ("Lost. The dealer got a blackjack.\n")

    elif total_in_hand(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print ("Busted. Loss.\n") 
    elif total_in_hand(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)                    
        print ("Dealer busts. Win!\n")
    elif total_in_hand(player_hand) < total_in_hand(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry. score isn't higher than the dealer. Loss.\n")

    elif total_in_hand(player_hand) > total_in_hand(dealer_hand):
        print_results(dealer_hand, player_hand)                    
        print ("Congratulations. Score is higher than the dealer. Win\n")              


def game():
    choice = 0
    #GAME START
    print ("**********************WELCOME TO BLACKJACK!*************************\n\n")

    dealer_hand = deal(deck)
    player_hand = deal(deck)

    while choice != "q":
        print("Enter a Choice.")
        main_choice =int(input('1.Enter 1 to See the Rules.\n2.Enter 2 to play Game.\n3.Enter 3 to Quit'))


        if(main_choice ==1):
            print('*****************************RULES****************\n')
            print('The objective of the game is to get as close to 21 points as possible without going over. ')
            print('Each round, the two players take turns throwing two dies as many times as they like and adding up the totals.')
            print('A player who has a total of more than 21 is considered bust and loses the game.')
            print('After each player has taken a turn, the player with the closest total to 21 wins the game.\n')
        
        #user chooses to Play
        elif(main_choice ==2):

            #print cards
            print('-------------------------------------------------')
            print ("The dealer is showing a " + str(dealer_hand[0]))
            print ("You have a " + str(player_hand) + " for a total of " + str(total_in_hand(player_hand)))
            print('-------------------------------------------------')
            
            #check for Blackjack Conditon
            blackjack(dealer_hand, player_hand)
            choice = input("1.Enter H or h for A hit.\n2.Enter S or s to Stand.\n3.Enter Q or q or 3 to Quit. ").lower()
            if choice == "h":
                hit(player_hand)
                while total_in_hand(dealer_hand) < 17:
                    hit(dealer_hand)
                score(dealer_hand, player_hand)
                play_again()
            elif(choice == "s"):
                while total_in_hand(dealer_hand) < 17:
                    hit(dealer_hand)
                score(dealer_hand, player_hand)
                play_again()
            elif choice == "q" or choice =='3':
                print ("Bye!")
                exit()
        #quit
        elif main_choice==3:
            print('Okay,Bye')
            exit()
        
if __name__ == "__main__":
    #call main
    game()
