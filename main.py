from turtle import Screen
import time
from player import Player
from car import Car
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


game_on = True
turtle = Player()
car_manager = Car()
score = Score()


screen.listen()
screen.onkey(turtle.move_player_up, 'Up')

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_on = False
            score.game_over()

    if turtle.at_finish_line():
        turtle.start()
        car_manager.increase_level()
        score.increase_level()

screen.exitonclick()