from turtle import Turtle,Screen
import random

# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.back(10)
#
# def rotate_clock():
#     tim.setheading(tim.heading()+10)
#
# def rotate_counter_clock():
#     tim.setheading(tim.heading()-10)
#
# def delete_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()







screen = Screen()
is_game_on = False
screen.setup(width=500,height=400)
user_guess = screen.textinput(title="Make a bet",prompt="Which turtle will win the race? Enter the color. ")
all_turtles = []

# screen.listen()
# screen.onkey(key="w",fun=move_forward)
# screen.onkey(key="s",fun=move_backward)
# screen.onkey(key="d",fun=rotate_counter_clock)
# screen.onkey(key="a",fun=rotate_clock)
# screen.onkey(key="c",fun=delete_drawing)

colors = ['red','orange','yellow','green','blue','purple']
y_position = [-70,-40,-10,20,50,80]

for turtle_index in range(0,6):
    # print(turtle_index)
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    # tim.forward(random.randint(1,10))
    all_turtles.append(new_turtle)

if user_guess:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won!, The {winning_color} turtle is the Winner!")
            else:
                print(f"You've lost!, The {winning_color} turtle is the Winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()