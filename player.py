from turtle import Turtle

STARTING_POSITION = (0, -280)
DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_player_up(self):
        self.forward(DISTANCE)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False

    def start(self):
        self.goto(STARTING_POSITION)