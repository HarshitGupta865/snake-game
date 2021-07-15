from turtle import Turtle, Screen

screen = Screen()

#To set the pop-up screen to required size
screen.setup(width=600, height=600)

#to set the backgroung color of pop-up screen
screen.bgcolor("black")

# to set title of the pop-up
screen.title("My Snake Game")

screen.tracer(0)


# 1.--------------------------------- CREATING THE SNAKE BODY--------------------------------------

# segment1 = Turtle(shape="square")
# segment1.color("white")
#
# segment2 = Turtle(shape="square")
# segment2.color("white")
# segment2.goto(-20, 0)
#
# segment3 = Turtle(shape="square")
# segment3.color("white")
# segment3.goto(-40, 0)


#Instead of declaring three segments separately, we created a for loop
starting_postions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_postions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


# 2. ----------------------------------MAKING THE BODY OF SNAKE MOVE---------------------------------

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)








screen.exitonclick()
