from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier",24,"normal")



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScoreBoard()
