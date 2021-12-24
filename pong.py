# Welcome to the code source code of the Pong Game 

import turtle 

win = turtle.Screen()
win.bgcolor("green")
win.title ("The Ping Pong Game In Python")
win.setup(width= 800, height = 600)
win.tracer(0)

# Score 
scorea= 0
scoreb= 0



#Paddle 1

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(stretch_len=1, stretch_wid=5)
paddle1.color("yellow")
paddle1.penup()
paddle1.goto(-350, 0)


#Paddle 2

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_len=1, stretch_wid=5)
paddle2.color("red")
paddle2.penup()
paddle2.goto(350, 0)


# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .2
ball.dy = .2

#Pen op 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto (0, 260)
pen.write("Player A: 0  Player B: 0",align="center", font=("Courier",24,"normal"))

# Function
# PADDLE 1
# up 

def paddle1_up():
    y = paddle1.ycor()
    y+=20
    paddle1.sety(y)

# down

def paddle1_down():
    y = paddle1.ycor()
    y-=20
    paddle1.sety(y) 


# PADDLE 2
# up
def paddle2_up():
    y=paddle2.ycor()
    y+=20
    paddle2.sety(y)

# down
def paddle2_down():
    y=paddle2.ycor()
    y-=20
    paddle2.sety(y)
    
# Keyboard keys for paddle 1

win.listen() 
win.onkeypress(paddle1_up,"w")

win.listen() 
win.onkeypress(paddle1_down,"s")

# Keyboard keys for paddle 2
win.listen()
win.onkeypress(paddle2_up, "Up")

win.listen()
win.onkeypress(paddle2_down, "Down")






# game loop to not crash the program
while True:
    win.update()

    # how to move the ball 
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1


    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        scorea +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scorea,scoreb),align="center", font=("Courier",24,"normal"))


    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*= -1
        scoreb+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scorea,scoreb),align="center", font=("Courier",24,"normal"))




 # paddle collions

    if (ball.xcor()>340 and ball.xcor()<350) and(ball.ycor()< paddle2.ycor()+40 and ball.ycor()>paddle2.ycor()-40):
        ball.setx(340) 
        ball.dx *=-1

    if (ball.xcor()<-340 and ball.xcor()>-350) and(ball.ycor()<paddle1.ycor()+40 and ball.ycor()>paddle1.ycor()-40):
        ball.setx(-340) 
        ball.dx *=-1





