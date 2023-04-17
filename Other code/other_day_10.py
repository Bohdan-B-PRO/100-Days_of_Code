# Functions with Output

# def format_name(f_name, l_name):
#     """Take a first and last name and format it ro return the title
#     case version of the name."""
#     if f_name == l_name:
#         return "You didn't provide valid input"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name}, {formated_l_name}"


# print(format_name(input("What's you first name? "), input("What's your last name? ")))


# Days in Month
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# def days_in_moth(year, month):
#     if month > 12 or month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]
#
#
# year = int(input("Enter a year "))
# month = int(input("Enter a month "))
# days = days_in_moth(year, month)
# print(days)








