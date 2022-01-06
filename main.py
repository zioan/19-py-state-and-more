from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
play = True


while play:
    def play_game():
        screen.clear()
        user_bet = screen.textinput(
            title="Make your bet", prompt="Whitch turtle will win the race? \n\n(red, orange, yellow, green, blue, purple)\n\nEnter a color: \n")
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]

        align = -125
        all_turtles = []

        for color in colors:
            new_turtle = Turtle(shape="turtle")
            new_turtle.penup()
            new_turtle.color(color)
            new_turtle.goto(x=-230, y=align)
            align += 50
            all_turtles.append(new_turtle)

        if user_bet:
            is_race_on = True

        while is_race_on:

            for turtle in all_turtles:
                if turtle.xcor() > 230:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    if winning_color == user_bet:
                        restart = screen.textinput(
                            title="You've won! \n", prompt=f"The {winning_color} turtle was the winner!\nNew game? (y/n) ")
                    else:
                        restart = screen.textinput(
                            title="You've lost! \n", prompt=f"The {winning_color} turtle was the winner!\nNew game? (y/n) ")

                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)

        if restart == 'y':
            play_game()
        else:
            screen.bye()

        screen.exitonclick()

    play_game()
