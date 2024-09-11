import turtle
import random

screen = turtle.Screen()
screen.colormode(255)

p1 = turtle.Turtle()
p2 = turtle.Turtle()
p3 = turtle.Turtle()
p4 = turtle.Turtle()
p5 = turtle.Turtle()

#ASK USER FOR BET:-
def prompt_user_for_bet():
    answer = screen.textinput("PUT YOUR BET","BLUE, GREEN, BROWN, ORANGE, RED")
    return answer

#GENERATE END LINE:-
def generate_endline():
    endline = turtle.Turtle()
    endline.hideturtle()
    endline.width(3)
    endline.up()
    endline.goto(300,-200)
    endline.down()
    endline.setheading(90)
    endline.color("grey")
    endline.forward(400)

#FUNCTION TO SET THE OBJECTS AT INITIAL PLACE:-
x = -300     #USED FOR SETTING INITIAL X COORDINATE OF A TURTLE OBJECT
y = -150     #USED FOR SETTING INITIAL Y COORDINATE OF A TURTLE OBJECT
def set_starting_place(p):
    global y
    p.up()
    p.goto(x,y)
    p.down()
    y+=75

#FUNCTION TO SET SHAPE AND COLOUR TO TURTLE OBJECTS AND SETTING THERE INITIAL PLACE:-
k=0
def add(p):
    global k
    color = ["red","orange","brown","green","blue"]
    p.shape("turtle")
    p.color(color[k])
    k+=1
    set_starting_place(p)

#FUNCTION TO START THE RACE AND FIND WINNER AND CHECK IF USER WON THE BET OR NOT
def start_race(bet):
    while True:
        p = random.choice([p1,p2,p3,p4,p5])
        p.speed(3)
        p.forward(5)
        position = p.pos()      #WILL RECEIVE A TUPLE LIKE (X,Y)
        if(position[0] == 300):
            winner_color = p.color()[0]        #p.color --> return ('red','red') tuple
            if bet == winner_color:
                print(f"YOU WON! {winner_color.upper()} IS THE WINNER")
            else:
                print(f"YOU LOSE! {winner_color.upper()} IS THE WINNER")
            break

def add_attributes():
    add(p1)
    add(p2)
    add(p3)
    add(p4)
    add(p5)

bet = prompt_user_for_bet()
add_attributes()
generate_endline()
start_race(bet)


screen.exitonclick()