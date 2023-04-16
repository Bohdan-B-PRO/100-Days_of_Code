# Printing
print("Hello World!")
print("Day 1 - Python Print Function.")
print("The function is declared like this:", end=" ")
print("print('what to print')")

# Printing and String Manipulation
print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sing.", end=" ")
print("E.p. print('Hello ' + 'World').", end=" ")
print("New lines can be created with a backslash and n.")
# print("Hello\nWorld")
# print("Hello" + " " + "Bohdan")

# Inputting
# input() will get user input in console
# Then print() will print the word, example: 'Hello' and the user input
print("Hello " + input("what's your name?"), end=" ")
print(len(input("What's your name? ")))

# Variable
user_name = input("What's your name? ")
length = len(user_name)
print(length)


# INDEPENDENT WORK

# 1. Create a greeting for your program.
print("Welcome to the band name generator.")
# 2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up in?in")
# 3. Ask the user for the name of a pet.
pet = input("What is the name of a pet?in")
print("Your band name is " + city + " " + pet)