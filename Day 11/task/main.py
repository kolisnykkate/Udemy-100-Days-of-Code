import random
from art import logo


CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ACE = CARDS [0]


def deal_card():
    card = random.choice(CARDS)
    return card

def is_blackjack(hand):
    return sum(hand) == 21

def is_over_21(hand):
    return sum(hand) > 21

def is_ace(card):
    return card == ACE

def comparison(user_hand, dealer_hand):
    if sum(dealer_hand) > sum(user_hand):
        print("Dealer wins. You lose!")
    elif sum(user_hand) > sum(dealer_hand):
        print("Congratulations! You win!")
    elif sum(user_hand) == sum(dealer_hand):
        print("It's a draw")
    print(f"Your final hand: {user_hand}, final score: {sum(user_hand)}.\n"
          f"Dealer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}.")


def game():

    while True:

        user_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]

        print(f"You cards: {user_hand}, current score: {sum(user_hand)}\n"
              f"Dealer's first car: {dealer_hand[0]}.")

        check = True
        while check:

            if is_over_21(user_hand):
                for i in range(len(user_hand)):
                    if is_ace(user_hand[i]):
                        user_hand[i] = 1
                        if is_over_21(user_hand):
                            print("You went over. You lose!")
                            return
                    else:
                        print("You went over. You lose.")
                        return

            if is_blackjack(dealer_hand):
                print("Dealer wins with a blackjack!")
                return
            if is_blackjack(user_hand):
                print("You win with a blackjack!")
                return

            draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw == "y":
                user_hand.append(deal_card())
                print(f"You cards: {user_hand}, current score: {sum(user_hand)}\n"
                      f"Dealer's first car: {dealer_hand[0]}.")

            if draw == "n":
                check = False


            while sum(dealer_hand)<17:
                dealer_hand.append(deal_card())


        comparison(user_hand, dealer_hand)
        break

def start_game():
    start = True
    while start:
        start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if start == "n":
            break
        else:
            print("\n" * 30)
            game()


########## Start #########

print(logo)
start_game()


