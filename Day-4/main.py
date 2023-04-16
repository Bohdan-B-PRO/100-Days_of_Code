# Randomisation and Python Lists
import random


# The main part

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]

user__choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
print(game_image[user__choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_image[computer_choice])

if user__choice >= 3 or user__choice < 0:
    print("You typed an invalid number, you lose!")
elif user__choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user__choice == 2:
    print("You lose!")
elif computer_choice > user__choice:
    print("You lose!!")
elif user__choice > computer_choice:
    print("You win!")
elif computer_choice == user__choice:
    print("It's a draw")













