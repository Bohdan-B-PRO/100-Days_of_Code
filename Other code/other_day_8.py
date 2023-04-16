# Function with inputs

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today")
#
# greet()

# Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#
# greet_with_name("")

# Function with name than 1 input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}?")
#
# # greet_with("Bohdan", "Nowhere")
# greet_with(location="Kharkiv", name="Bohdan")


# Area Calc
# import math
#
# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_cons = math.ceil(area / cover)
#     print(f"You'll need {num_of_cons} cans of paint.")
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime Number Checker
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number - 1):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number!")
#     else:
#         print("I't a prime number!")
#
# n = int(input("Check this number: "))
# prime_checker(number=n)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
            shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")


# def encrypt(plain_text, shift_amount):
#     cipher_text =""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encode text is {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decode text is {plain_text}")
#
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)








