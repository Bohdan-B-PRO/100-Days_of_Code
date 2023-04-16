# Tickets to the rollercoaster
# print("Welcome to the rollercoaster!")
# height = int(input("What's your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride in rollercoaster")
#     age = int(input("What's your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to br ok. Mave a free ride on as")
#     else:
#         bill = 12
#         print("Adult rickets are $17")
#
#     wants_photo = input("Do you want a photo taken? Yes or No ")
#     if wants_photo == "Yes":
#         bill += 3
#
#     print(f"Your final bill is {bill}")
#
# else:
#     print("Sorry? you have to grow taller before yon can ride.")


# BIM Calculator 2.0
# height = int(input("Enter your height in m: "))
# weight = int(input("Enter your weight in kg: "))
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, you're underweight!")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you have a normal weight!")
# elif bmi < 30:
#     print(f"Your bmi is {bmi}, you're overweight!")
# elif bmi < 35:
#     print(f"Your bmi is {bmi}, you're obese!")
# else:
#     print(f"Youe bmi is {bmi}, you're clinical obese!")


# Love Calculator
# print("Welcome to the Love Calculator!")
# name_1 = input("What's your name? \n")
# name_2 = input("What's their name? \n")
# combined_string = name_1 + name_2
# lower_case_string = combined_string.lower()
#
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
#
# true = t + r + u + e
#
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
#
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
# print(love_score)
#
# if (love_score < 10) or (love_score > 90):
#     print(f"Your love score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"You score is {love_score}, you're alright together")
# else:
#     print(f"Your score is {love_score}")


# Leap day
# year = int(input("Which year do you want to check "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year!")
#         else:
#             print("Not leap year!")
#     else:
#         print("Not leap year!")
# else:
#     print("Not leap year!")


# # Pizza Oder
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L ")
# add_pepperoni = input("Do you want pepperoni? Yes or No ")
# extra_cheese = input("Do you want extra cheese? Yes or No ")
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
#
# if add_pepperoni == "Yes":
#     if size == "S":
#         bill += 2
#     else:
#         bill = 3
#
# if extra_cheese == "Yes":
#     bill += 1
#
# print(f"Your final bill is ${bill}")


# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
#
# first = input("Left or right?\nType Right/Left: ").lower()
# if first == "right":
#   print('''                      -     =    .--._
#                 - - ~_=  =~_- = - `.  `-.
#               ==~_ = =_  ~ -   =  .-'    `.
#             --=~_ - ~  == - =   .'      _..:._
#            ---=~ _~  = =-  =   `.  .--.'      `.
#           --=_-=- ~= _ - =  -  _.'  `.      .--.:
#             -=_~ -- = =  ~-  .'      :     :    :
#              -=-_ ~=  = - _-`--.     :  .--:    D
#                -=~ _=  =  -~_=  `;  .'.:   ,`---'@
#              --=_= = ~-   -=   .'  .'  `._ `-.__.'
#             --== ~_ - =  =-  .'  .'     _.`---'
#            --=~_= = - = ~  .'--''   .   `-..__.--.
#              --==~ _= - ~-=  =-~_-   `-..___(  ===;
#           --==~_==- =__ ~-=  - -    .'       `---'
#   ''')
#   print("Sonic got the treasure before you, try again.")
# elif first == 'left':
#   print('''
#    _
#   | |
#   | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __
#   | __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \
#   | |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
#   \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/
#                                                         | |
#                                                         |_|
#   ''')
#   print("Nice, you made it to the next level!")
#
#   second = input("Your map shows that you need to get to Treasure Island, you can wait to board a ship or swim accross the sea, pick one.\nType Swim/Wait: ").lower()
#   if second == "swim":
#     print('''
#                     (`.
#                     \ `.
#                       )  `._..---._
#     \`.       __...---`         o  )
#     \ `._,--'           ,    ___,'
#       ) ,-._          \  )   _,-'
#     /,'    ``--.._____\/--''
#         ''')
#     print("Unfortunately, you were eaten by a Great White Shark, try again.")
#   elif second == "wait":
#     print("Nice, you made it to the next level, you're pretty good at this!")
#     print ("Welcome to:")
#     print ('''
#      _                                     _     _                 _
#     | |                                   (_)   | |               | |
#     | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
#     | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
#     | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
#     \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
#     ''')
#
#     third = input("Now that you've made it to Treasure Island, you can dig or search the cave. \n Type Dig/Cave: ").lower()
#     if third == "dig":
#       print("You've found the treasure, you win!")
#     elif third == "cave":
#       print('''
#       _
#       | |
#       | |__   ___  __ _ _ __
#       | '_ \ / _ \/ _` | '__|
#       | |_) |  __/ (_| | |
#       |_.__/ \___|\__,_|_|
#                   ''')
#       print("You were eaten by a bear, game over.")


