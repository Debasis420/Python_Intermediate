from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():    # W
    tim.forward(10)

def move_backwards():   # S
    tim.backward(10)

def turn_left():        # A
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():       # D
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():            # C
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()

