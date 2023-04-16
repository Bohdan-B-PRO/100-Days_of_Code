# Hangman Project

word_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly chose a word from the word_list and assign it a variable
#  called chosen_word
import random

chosen_word = random.choice(word_list)
lives = 6

# TODO-2 Ask the user to guess a letter and assign their answer to a variable
#  called guess. Make guess lowercase
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

# TODO-3 Check in the letter the user guessed (guess) is one of the leters
#  in the chosen_word
for position in range(word_length):
    letter = chosen_word[position]
    # print(f"Current position {position}\n Current letter: {letter}\n Current Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter
    else:
        print("No much")
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
print(display)
if "_" not in display:
    end_of_game = True
    print("You win")






