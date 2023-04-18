################### Blackjack Project############################

#Difficulty Normal © Use all Hints below to complete the project.
#Difficulty Hard : Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard : Only Use Hints 1 & 2 to complete the project.
#Difficulty Expert •: pnly use Mint 1 to complete the project
# Our Blackjack House Rules
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
#* Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.


########################## Mints ##################################
# mint 1: Go to this website and try oat the Blackjack https://ganes.washingtonpost.con/ganes/blackjack/
# Then try out the completed stockJack project here:
# https://blackjack-final.apporewery.repl.run

# mint 2 Read this breakdown of progras regairenents!
# http://listmoz.com/view/Gh340)pvJ8FVRIZJvxf

# To treate your won ttorciant for the pregras.
# mint 3: Download and read this flow chart l've created:
# https://drive.soogle.com/uc?export-downlosd518-1rokiNCrhar9eX7u7y|MI@SuyEk-rPnt

# mint 4: Create a deal card) function that uses the list below to
# oreturns a randos card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


### Trial code ###

# import clear
# import random
# from art import logo
#
# def deal_card():
#     """Return a random card from the deck"""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
#
# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#         return sum(cards)
#
#
# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return "Oraw"
#     elif computer_score == 0:
#         return "Lose, opponent has blackjack"
#     elif user_score == 0:
#         return "Win with a blackjack"
#     elif user_score == 21:
#         return "You went over, You lose"
#     elif computer_score == 21:
#         return "Opponent went over, You win"
#     elif user_score > computer_score:
#         return "You win"
#     else:
#         return "You lose"
#
# def play_game():
#     print(logo)
#     user_cards = []
#     computer_cards = []
#     is_game_over = False
#
#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#
#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"  Your card: {user_cards}, current score: {user_score}")
#         print(f"  Computer's first card: {computer_cards[0]}")
#
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card , type 'n' to pass ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True
#
#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)
#
#     print(f"  Your final hand: {user_cards}, final score:{user_score}")
#     print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     clear()
#     play_game()



