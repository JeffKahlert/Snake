from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score(0)
screen.listen()
screen.onkeyrelease(key="Up", fun=snake.move_up)
screen.onkeyrelease(key="Right", fun=snake.move_right)
screen.onkeyrelease(key="Left", fun=snake.move_left)
screen.onkeyrelease(key="Down", fun=snake.move_down)

game_loop = True

while game_loop:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_up()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 \
            or snake.head.ycor() < -290:
        game_loop = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_loop = False
            score.game_over()

screen.exitonclick()