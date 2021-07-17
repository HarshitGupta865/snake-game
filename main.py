import time
from turtle import Turtle, Screen

screen = Screen()

# To set the pop-up screen to required size
screen.setup(width=600, height=600)

# to set the background color of pop-up screen
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


# Instead of declaring three segments separately, we created a for loop
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# 2. ----------------------------------MAKING THE BODY OF SNAKE MOVE---------------------------------

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # By this code we make the blocks of snake body follow the block that is ahead of it.
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)



screen.exitonclick()
