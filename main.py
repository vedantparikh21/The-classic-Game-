from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WALL_X = 400
WALL_Y = 400
COLLIDE_X = WALL_X -20
COLLIDE_Y = WALL_Y - 80


screen = Screen()
screen.screensize(WALL_X,WALL_Y)
screen.bgcolor('black')
screen.title('That similar Nokia 🐍 Game!')
screen.tracer(0) # turn animation off - 0
# print(screen.screensize())


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up,'Up')
screen.onkey(snake.up,'w')
screen.onkey(snake.down,'Down')
screen.onkey(snake.down,'s')
screen.onkey(snake.right,'Right')
screen.onkey(snake.right,'d')
screen.onkey(snake.left,'Left')
screen.onkey(snake.left,'a')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # check food collision
    if snake.head.distance(food) <=15: 
        food.go_random_location()
        scoreboard.scorepoint()
        snake.extend()

    # detect wall collision
    if (snake.head.xcor() > COLLIDE_X or snake.head.xcor() < -COLLIDE_X or 
        snake.head.ycor() > COLLIDE_Y or snake.head.ycor() < -COLLIDE_Y):
        game_is_on = False
        scoreboard.game_over()

    # detect collision with the same body
    for segment in snake.snake_block[1 : ]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()