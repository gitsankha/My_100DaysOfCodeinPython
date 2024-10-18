import random
import art

all_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def calculate_score(lst_of_cards):
    """Evaluates hand of either user or computer"""
    if len(lst_of_cards) == 2:
        if sum(lst_of_cards) == 21:
            return 0
    if 11 in lst_of_cards:
        if sum(lst_of_cards) > 21:
            index_of_ace = lst_of_cards.index(11)
            lst_of_cards[index_of_ace] = 1
    return sum(lst_of_cards)

def deal_card():
    """Return a random card from all the cards"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def compare(user_score , computer_score):
    """Prints out the result of a session"""
    if user_score == computer_score:
        print("Draw")
    elif computer_score == 0:
        print("You Lose")
    elif user_score == 0:
        print("Blackjack. You win. :)")
    elif user_score > 21:
        print("You went over. You lose :/")
    elif computer_score > 21:
        print("You win . Dealer's got a bust.")
    else:
        if computer_score > user_score:
            print("You Lose.")
        else:
            print("You win.")

user_wishes_to_play = 'y'

while user_wishes_to_play == 'y':
    print(art.logo)

    user_cards = random.choices(all_cards , k = 2)
    computer_cards = random.choices(all_cards , k = 2)

    print(f"Your cards: {user_cards}.Current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    user_cards_score = calculate_score(user_cards)
    computer_cards_score = calculate_score(computer_cards)
    while user_cards_score != 0 and computer_cards_score != 0 and user_cards_score < 21 and computer_cards_score  < 21:
        user_wants_to_draw = input("Type 'y' to get another card , type 'n' to pass: ")
        if user_wants_to_draw == 'y':
            user_cards.append(deal_card())
            print(f"Your cards: {user_cards} , current score: {calculate_score(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
        else:
            break
        user_cards_score = calculate_score(user_cards)
    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    print(f"Your final hand : {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand : {computer_cards}, final score: {calculate_score(computer_cards)}")
    compare(calculate_score(user_cards), calculate_score(computer_cards))
    user_wishes_to_play = input("Do you wish to play again? 'y' or 'n': ")
