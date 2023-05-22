from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "bogdanburduluk@gmail.com"
MY_PASSWORD = "password"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"Latter_templates/latter_{random.randint(1, 3)}.txt"
    with open(file_path) as latter_file:
        contents = latter_file.read()
        contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subjeck:Happy birthday!\n\n{contents}"
        )









