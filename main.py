from turtle import Turtle,Screen
import random
y_positions=[-100,-50,0,50,100,150]
colours = ["red","blue","orange","green","black","pink"]
screen=Screen()
screen.setup(500,500)
user_bet=screen.textinput("Make your bet:","Choose your color:")
if user_bet not in colours:
    print("Invalid Bet")
    exit()
    
if user_bet:
    is_on=True
all_turtle=[]
colors=["red","blue","orange","green","black","pink"]
for turtle in range(0,6):
            
    my_turtle=Turtle(shape="turtle")
    my_turtle.color(colors[turtle])
    my_turtle.penup()
    my_turtle.goto(-240,y_positions[turtle])
    all_turtle.append(my_turtle)
    


while is_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_on=False
            winning_color=turtle.fillcolor()
            if winning_color==user_bet:
                print("Congratulations you have won the race!!")
            else :
                print(f"Sorry you loose the bet.The winnner is {winning_color}")
            break
        distance=random.randint(5,20)
        turtle.fd(distance)

screen.exitonclick()