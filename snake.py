from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_POSITION = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_block = []
        self.create_snake()
        self.head = self.snake_block[0] # positioning done such that this line is below create_snakes method as the body gets created
                                         # and we are able to access the snake_block bcoz it wont be empty

    def create_snake(self):
        for position in POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        snake_body = Turtle(shape='square')
        snake_body.pu()
        snake_body.color('white')
        snake_body.goto(position)
        self.snake_block.append(snake_body)

    def extend(self):
        self.add_body(self.snake_block[-1].position()) # get turtle's current location
        # pass

    def move(self):
        for snake_num in range(len(self.snake_block)-1,0,-1):
            new_x = self.snake_block[snake_num-1].xcor()
            new_y = self.snake_block[snake_num-1].ycor()
            self.snake_block[snake_num].goto(new_x,new_y)
        self.head.forward(MOVE_POSITION)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 
