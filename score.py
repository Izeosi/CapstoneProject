from turtle import Turtle

FONT = ('Arial', 15, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'level: {self.level}', align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER', align='left', font= FONT)