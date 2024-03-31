import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
score = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()
    # collision with car_manager
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # detect final position
    if player.is_at_end():
        player.go_to_start()
        car_manager.level_up()
        score.update_score()


