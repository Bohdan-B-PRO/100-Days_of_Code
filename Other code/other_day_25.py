# with open("weather_data_day-25.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data_day-25.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "Temp":
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas


data = pandas.read_csv("weather_data_day-25.csv")
# print(data["Temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["Temp"].to_list
# print(temp_list)
#
# print(data["Temp"].mean())
# print(data["Temp"].max())
#
# print(data["Condition"])
# print(data.Condition)

print(data.Day == "Monday")
print(data[data.Temp == data.Temp.max()])

# monday = data[data.Day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp + 9/5 - 32
# print(monday_temp_f)

data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data_day_25.csv")










