import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = Car()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.up,"w")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_car:
        if car_manager.distance(player) <20:
            is_on=False
            score.game_over()

    if player.at_finish_line():
        player.up()
        car_manager.level_up()
        score.update_score()




screen.exitonclick()