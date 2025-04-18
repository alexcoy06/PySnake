import time
from turtle import Screen
from lib.food import Food
from lib.snake import Snake
from lib.scoreboard import Scoreboard

# GUI Step-up for the Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Event listening for button presses   
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.right, 'd')

# The functioning game
game_on = True
while game_on:
    
    #smoothing movement transition
    screen.update()
    time.sleep(0.15)
    snake.move()
    
    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.eaten()
        snake.extend()
        scoreboard.scored()
        
    
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    elif any(snake.head.distance(segment) < 10 for segment in snake.snake_body[1:]):
        game_on = False
        scoreboard.game_over()

    
screen.exitonclick()