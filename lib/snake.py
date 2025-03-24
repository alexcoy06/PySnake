from turtle import Turtle

# Constants for key values
DISTANCE = 20
BODY_LENGTH = 3

class Snake:
    
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    
    # Creates the body with length across the x    
    def create_snake(self):
        for segment in range(BODY_LENGTH):
            self.add_segment((-segment * DISTANCE, 0))
        
    
    def add_segment(self, position):
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.snake_body.append(new_segment)
            
    def extend(self):
        self.add_segment(self.snake_body[-1].position())
    
    # Snake Movement so that all segments moves in line     
    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(DISTANCE)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)