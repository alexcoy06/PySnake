from turtle import Turtle

ALIGN ='center'
FONT =('Terminal', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)
        
    
    def scored(self):
        self.score += 1
        self.clear()
        self.update_score()
        