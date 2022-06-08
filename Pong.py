# window.tracer(number) basically stops the window from updating so that you have to manually update it and it will speed up the game a bit
# window.listen and window.onkeypress is for the window to listen for key inputs 
#  ball.movey *= -1 means that the ball will move in the negative direction
# import winsound is a module for sounds

import turtle
import time
import winsound 


HEIGHT = 600
WIDTH = 800

window = turtle.Screen()
window.title("Fan-Made Pong")
window.bgcolor("black")
window.setup(width=WIDTH, height=HEIGHT)
window.tracer(0)

# Paddles

SW = 5
SL = 0.3

class Paddle:
    def __init__(self, xpos, ycor):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=SW, stretch_len=SL)
        self.paddle.penup()
        self.paddle.goto(xpos, ycor)

# Left Paddle

leftpaddle = turtle.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=SW, stretch_len=SL)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Right Paddle

rightpaddle = turtle.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=SW, stretch_len=SL)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Functions

def leftpaddle_up():
    y = leftpaddle.ycor()
    y += 30
    leftpaddle.sety(y)
def leftpaddle_down():
    y = leftpaddle.ycor()
    y -= 30
    leftpaddle.sety(y)

def rightpaddle_up():
    y = rightpaddle.ycor()
    y += 30
    rightpaddle.sety(y)

def rightpaddle_down():
    y = rightpaddle.ycor()
    y -= 30
    rightpaddle.sety(y)

# Keyboard Binds

window.listen()

window.onkeypress(leftpaddle_up, "w")
window.onkeypress(leftpaddle_down, "s")

window.onkeypress(rightpaddle_up, "Up")
window.onkeypress(rightpaddle_down, "Down")

# Score

scorea = 0
scoreb = 0 
        
# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.movex = 0.5
ball.movey = 0.5

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {} / Player 2: {}".format(scorea, scoreb), align="center", font=("courier", 24, "normal"))

# Game Loop

while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.movex)
    ball.sety(ball.ycor() + ball.movey)
    # Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.movey *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.movey *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 410:
        time.sleep(0.5)
        ball.goto(0, 0)
        ball.movex *= -1
        scorea += 1
        pen.clear()
        pen.write("Player 1: {} / Player 2: {}".format(scorea, scoreb), align="center", font=("courier", 24, "normal"))
    if ball.xcor() < -410:
        time.sleep(0.5)
        ball.goto(0,0)
        ball.movex *= -1
        scoreb += 1
        pen.clear()
        pen.write("Player 1: {} / Player 2: {}".format(scorea, scoreb), align="center", font=("courier", 24, "normal"))

    # Ball and Paddle Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ball.movex *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() < 350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ball.movex *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)