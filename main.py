import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

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

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 3. Controlling the movement of snake

# Putting event listener
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 2. ----------------------------------MAKING THE BODY OF SNAKE MOVE---------------------------------

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # detect collision with tail
    # if head collides with any segment in the tail trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
