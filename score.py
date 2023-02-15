from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.update_score()
