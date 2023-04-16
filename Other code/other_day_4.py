# random_integer = random.randint(1, 10)
# print(random_integer)
#
# # 0.0000000...-0.9999999999....
# random_float = random.random() * 5
# print(random_float)
#
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")


# Heads or Tails
# test_seed = int(input("Create a seed number: "))
# random.seed()
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")


# Lists
# states_of_america = ["Delaware", "Pennsylvania"]
# states_of_america.append("Pennsylvania-1")
# states_of_america.extend(["NewYork", "Jack Bauer Land"])
# print(states_of_america)


# Treasure Map
# row1 = ["=)", "'_'", "=}"]
# row2 = ["=)", "'_'", "=}"]
# row3 = ["=)", "'_'", "=}"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Were do you want to put the treasure? ")
# horizontal = int(position[0])
# vertical = int(position[1])
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"

# Who's Paying?
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# name_as_CSV = input("Give me everybody's names, seperated by a coma. ")
# names = name_as_CSV.split(", ")
# num_items= len(names)
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + "is going to buy the meal today!")