from turtle import *
import random
screen=Screen()
screen.setup(width=500,height=500)
screen.bgcolor("black")

color=["red","green","blue","yellow","cyan","pink"]
ypos=[-100,-50,0,50,100,150]
game_list=[]
for i in range(0,6):
    turtle = Turtle("turtle")
    turtle.shapesize(2)
    turtle.color(color[i])
    turtle.setposition(x=-230,y=ypos[i])
    game_list.append(turtle)

game=True
user=screen.textinput("BET GAME","Enter the Color you Bet:")
if user:
    game=False
while not game:
    for i in game_list:
        speed = random.randint(0, 15)
        i.forward(speed)
        if i.xcor()>250:
            winner=i.pencolor()
            game = True
            if user==winner:
                print("You won")
            else:
                print(f"You lost the winner is {winner}")

screen.exitonclick()