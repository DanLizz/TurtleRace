import turtle
from turtle import *
import random

screen = Screen()
screen.setup(height=500, width=400)
guess = turtle.textinput(title="Guess", prompt="Which turtle is going to win the race? Input the color: ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

is_race_on = False
all_turtles = []

for t_no in range(0, 7):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[t_no])
    new_turtle.penup()
    ty = -100 + t_no*25
    new_turtle.goto(x= -190, y= ty)
    all_turtles.append(new_turtle)

if guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 150:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == guess.lower():
                print("You Win")
            else:
                print("You lose")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
