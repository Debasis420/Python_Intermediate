from turtle import Turtle, Screen

tim = Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

my_screen = Screen()
my_screen.exitonclick()
