from tkinter import *


def miles_to_km():
    calc_num = float(num_miles.get()) * 1.609
    answer_label.config(text=round(calc_num, 2))


window = Tk()
window.title("Miles to KM")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles", font="Arial")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

km_label = Label(text="KM", font="Arial")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

equal_label = Label(text="Equals", font="Arial")
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

answer_label = Label(text="0", font="Arial")
answer_label.grid(column=1, row=1)
answer_label.config(padx=10, pady=10)

num_miles = Entry(width=10)
num_miles.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()


# from tkinter import *
#
# def miles_to_km():
#     miles = float(miles_input.get())
#     km = round(miles * 1.689)
#     kilometer_result_label.config(text=f"{km}")
#
# window = Tk()
# window.title("Miles to kilometer Converter")
# window.config(padx=2, pady=20)
#
# miles_input = Entry(width=7)
# miles_input.grid(column=1, row=0)
#
# miles_later = Label(text="Miles")
# miles_input.grid(column=2, row=0)
#
# is_equal_label = Label(text="is equal to")
# is_equal_label.grid(column=0, row=1)
#
# kilometer_result_label = Label(text="0")
# kilometer_result_label.grid(column=1, row=1)
#
# kilometer_label = Label(text="Km")
# kilometer_label.grid(column=2, row=1)
#
# calculate_button = Button(text="Button", command=miles_to_km)
# calculate_button.grid(column=1, row=2)
#
#
# window.mainloop()