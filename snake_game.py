from turtle import Screen, Turtle
from snake import Snake
import time

# GUI Step-up for the Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()

# The functioning game
game_on = True
while game_on:
    #smoothing movement transition
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
screen.exitonclick()