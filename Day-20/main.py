from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mt snake game")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.listen()
screen.onkey(snake.up, "up")
screen.onkey(snake.down, "down")
screen.onkey(snake.left, "left")
screen.onkey(snake.right, "right")


screen.exitonclick()

