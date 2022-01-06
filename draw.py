from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_right():
    tim.right(10)

# OR


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear():
    screen.reset()


screen.listen()
screen.onkeypress(key='w', fun=move_forwards)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='c', fun=clear)

screen.exitonclick()
