# from turtle import Turtle,Screen
# import random
# screen=Screen()
# screen.setup(500,500)
# tim=Turtle()
# bet_color=screen.textinput("Make your bet","Choose your turtle by entering their color:")
# is_on=True
# colors=["green","blue","yellow","red","purple","black"]
# y_position=[-100,-50,0,50,100,150]
# all_turtle=[]
# if bet_color:
#     is_on=True
# for i in range(0,6):
    
#     tim=Turtle(shape="turtle")
#     tim.color(colors[i])
#     tim.penup()
#     tim.goto(-240,y_position[i])
#     all_turtle.append(tim)
# while is_on:
#     for turtle in all_turtle:
#         if turtle.xcor()>240:
#             is_on=False
#             winning_color=turtle.color()
#             if winning_color==bet_color:
#                 print("You won!")
#             else :
#                 print(f"You losse the winner is {winning_color[0]}")
#         distance=(random.randint(5,20)) 
#         turtle.fd(distance)    
# screen.exitonclick()

from turtle import Turtle,Screen
import random
y_positions=[-100,-50,0,50,100,150]
colours = ["red","blue","orange","green","black","pink"]
screen=Screen()
screen.setup(500,500)
user_bet=screen.textinput("Make your bet:","Choose your color:")
if user_bet not in colours:
    print("Chutiya nikal yaha se")
    exit()
    
if user_bet:
    is_on=True
all_turtle=[]
# colors=["red","blue","orange","green","black","pink"]
# for turtle in range(0,6):
            
#     my_turtle=Turtle(shape="turtle")
#     my_turtle.color(colors[turtle])
#     my_turtle.penup()
#     my_turtle.goto(-240,y_position[turtle])
#     all_turtle.append(my_turtle)
    
for position,colour in [(-100,"red"),(-50,"blue"),(0,"orange"),(50,"green"),(100,"black"),(150,"pink")]:
    turtle = Turtle(shape="turtle")
    turtle.color(colour)
    turtle.penup()
    turtle.goto(-240, position)
    all_turtle.append(turtle)
    
    


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