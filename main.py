from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(500,500)
tim=Turtle()
bet_color=screen.textinput("Make your bet","Choose your turtle by entering their color:")
is_on=True
colors=["green","blue","yellow","red","purple","black"]
y_position=[-100,-50,0,50,100,150]
all_turtle=[]
if bet_color:
    is_on=True
for i in range(0,6):
    
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-240,y_position[i])
    all_turtle.append(tim)
while is_on:
    for turtle in all_turtle:
        if turtle.xcor()>240:
            is_on=False
            winning_color=turtle.color()
            if winning_color==bet_color:
                print("You won!")
            else :
                print(f"You losse the winner is {winning_color[0]}")
        distance=(random.randint(5,20)) 
        turtle.fd(distance)    
screen.exitonclick()