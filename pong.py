# joguinho simples de pong
import turtle
import os

win = turtle.Screen()
win.title("Pong @jiniciusvulio")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# score
score_a = 0
score_b = 0

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.09
ball.dy = 0.09

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player1: 0  Player2: 0", align="center", font=("Courier", 24, "normal"))

# functions
def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

# keybinds
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
  win.update()

  # ball movements
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # border checking
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
    os.system("aplay bounce.wav&")

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1
    os.system("aplay bounce.wav&")

  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    score_a += 1
    pen.clear()
    pen.write("Player1: {}  Player2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    score_b += 1
    pen.clear()
    pen.write("Player1: {}  Player2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

  # collision events
  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
    ball.setx(-340)
    ball.dx *= -1
    os.system("aplay bounce.wav&")

  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
    ball.setx(340)
    ball.dx *= -1
    os.system("aplay bounce.wav&")