# Dictionaries & Nesting
# programing_dictionary = {"Bug": "An error is a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again.",
#                           "Loop": "The action of doing something over and over again.",
#                          }

# Retrieving items from dictionary
# print(programing_dictionary["Function"])

# Adding new items to dictionary
# programing_dictionary["Loop"] = "The action of doing something over and over again."
# print(programing_dictionary)

# Create an empty dictionary
# empty_dictionary = {}

# Wipe an existing dictionary
# programing_dictionary = {}
# print(programing_dictionary)

# Edit an item in a dictionary
# programing_dictionary["Bug"] = "A moth in your computer"
# print(programing_dictionary)

# Loop through a dictionary
# for key in programing_dictionary:
#     print(key)
#     print(programing_dictionary[key])


# Grading Program
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# # TODO-1 Create on empty dictionary called student_grades
# student_grades = {}
#
# # TODO-2 Write your code below to add the grades to student_grades
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectation"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)


# Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# Nesting a list in a Dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany":  {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# Nesting Dictionary in list
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     },
# ]
#
# def add_new_country(country_visited, times_visited, cities_visited,):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)





