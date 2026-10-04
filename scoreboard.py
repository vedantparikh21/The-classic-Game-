from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier',24,'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.highscore = self.fetch_highscore()
        self.shapesize(stretch_len=1.5,stretch_wid=1.5)
        self.hideturtle()
        self.goto(0,290)
        self.color('White')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score = {self.score}, High Score = {self.highscore}',False,ALIGNMENT,font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('high_score.txt',mode='w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def fetch_highscore(self):
        with open('high_score.txt') as file:
            return int(file.read())

    def scorepoint(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER!',False,ALIGNMENT,font=FONT)
    