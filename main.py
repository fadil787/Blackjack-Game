import random

import art
from art import logo




def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def score_calc(lists):
    if sum(lists) == 21 and len(lists) == 2:
        return 0;
    if sum(lists) > 21 and 11 in lists:
        lists.remove(11)
        lists.append(1)
    return sum(lists)


def compare(u_score,c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You Lose, Opponent with Blackjack"
    elif u_score == 0:
        return "You win with Blackjack"
    elif u_score > 21:
        return "Over 21!, You Lose"
    elif c_score > 21:
        return "Opponent over 21, You Win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You Lose"







def play_game():
    print(art.logo)
    user = []
    computer = []
    user_score = -1
    computer_score = -1
    is_game_over = False
    for i in range(2):
        user.append(draw_card())
        computer.append(draw_card())

    while not is_game_over:

        user_score = score_calc(user)
        computer_score = score_calc(computer)
        print(f"your cards : {user}, current score: {user_score}\n computer's first card : {computer[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("enter 'y' for new card or 'n' for pass")
            if choice == 'y':
                user.append(draw_card())
            else:
                is_game_over : True


    while computer_score != 0 and computer_score < 17:
        computer.append(draw_card())
        computer_score=score_calc(computer)

    print(f"your cards : {user} and your score : {user_score}\n computer's cards: {computer} and computer's score : {computer_score}")
    print(compare(user_score,computer_score))

while (input("Do you like to play a game of blackjack 'y' or 'no' ")) == 'y':
    print("\n"*50)
    play_game()