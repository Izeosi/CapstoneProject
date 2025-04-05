from turtle import Turtle
import random

COLORS = ['red', 'green', 'yellow', 'blue', 'orange', 'purple']
STARTING_DISTANCE = 5
DISTANCE_INCREMENT = 5

class Car:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_DISTANCE


    def create_car(self):
        random_int = random.randint(1,6)
        if random_int == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_level(self):
        self.car_speed += DISTANCE_INCREMENT

