# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("SeaGreen")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# Один из вариантов как нарисовать графичиский квадрат
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)

# screen = Screen()
# screen.exitonclick()


import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# TChallenge 1
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


colours = ["dark turquoise", "turquoise", "dark cyan", "sea green", "dodger blue", "olive drab", "deep sky blue", "hot pink"]

# Challenge 2
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# Challenge 3/4/5

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # random_color = (r, g, b)  # For challenge 4
    # return random_color  # For challenge 4
    color = (r, g, b)
    return color

directions = [0, 90, 100, 270]
# tim.pensize(15)  # For challenge 4
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())  # For challenge 5
        tim.circle(100)  # For challenge 5
        tim.setheading(tim.heading() + 10)  # For challenge 5

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()




# for _ in range(200):  # For chalenge 4
#     tim.color(random_color())  # For chalenge 4
#     tim.forward(30)  # For chalenge 4
#     tim.setheading(random.choice(directions))  # For chalenge 4







