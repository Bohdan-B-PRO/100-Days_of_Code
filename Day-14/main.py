from art import logo, vs
from game_data import data
import random
from clear import clear

def format_data(account):
    """Format the account data into printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# Display art
print(logo)
score = 0
game_should_continue = True
# Generate a randon account from the game data
account_B = random.choice(data)

# Make the game repeatable
while game_should_continue:


    # Making account at position B become the next account at position A
    account_A = account_B
    account_B = random.choice(data)
    if account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Against A: {format_data(account_B)}")

    # Ask user for game
    guess = input("How has mare followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower count of each account
    a_follower_count = account_A['follower_count']
    b_follower_count = account_B['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    clear()

    # Give user feedback on their game
    ## Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong! Final score: {score}.")










