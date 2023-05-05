with open("my_file(day 24).txt") as file:
    contents = file.read()
    print(contents)

with open("New_file(day 24).txt", mode="a") as file:
    file.write("\nNew text")
