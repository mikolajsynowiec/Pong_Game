from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_1, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.score_2, align=ALIGNMENT, font=FONT)


    def add_point_1(self):
        self.score_1 += 1
        self.update_scoreboard()


    def add_point_2(self):
        self.score_2 += 1
        self.update_scoreboard()



