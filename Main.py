import art
import random


def generate_cards():
    """Generating random cards from the given deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return '\nDraw'
    elif computer_score == 0:
        return '\nUser loses. Computer has "BLACKJACK"'
    elif user_score == 0:
        return '\nUser wins. It`s a "BLACKJACK"'
    elif user_score > 21:
        return '\nYou went over, You lose'
    elif computer_score > 21:
        return '\nOpponent went over, You win'
    elif user_score > computer_score:
        return '\nYou win'
    else:
        return '\nYou lose'

def play_game():
    computer_cards = []
    user_cards = []
    is_game_over = False
    print(art.logo)


    for i in range(2):
        """Distributing cards to user and computer"""
        computer_cards.append(generate_cards())
        user_cards.append(generate_cards())

    while not is_game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"User's  cards: {user_cards}, User's score: {user_score}")
        print(f"Computer's  card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        user_choice_for_more_cards = input("Want to draw another card? Type 'y' for Yes and 'n' for No: ")
        if user_choice_for_more_cards == 'y':
            user_cards.append(generate_cards())
        else:
            is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(generate_cards())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Wanna play a game of BLACKJACK. Type 'y' to continue and 'n' to terminate: ") == 'y':
    play_game()