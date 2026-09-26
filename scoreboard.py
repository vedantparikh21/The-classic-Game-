from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier',24,'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shapesize(stretch_len=1.5,stretch_wid=1.5)
        self.hideturtle()
        self.goto(0,290)
        self.color('White')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score = {self.score}',False,ALIGNMENT,font=FONT)

    def scorepoint(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER!',False,ALIGNMENT,font=FONT)
    