from turtle import Turtle
SEGMENTS_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
        self.head.shape("square")
        
    def createSnake(self):
        for position in SEGMENTS_POSITIONS:
            self.addSegment(position)

    def addSegment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def resetSnake(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]

    def extend(self):
        self.addSegment(self.segments[-1].position())

    def move(self):
        for num_seg in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[num_seg - 1].xcor()
            new_y = self.segments[num_seg - 1].ycor()
            self.segments[num_seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
         if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
         if self.head.heading() != LEFT:
            self.head.setheading(0)