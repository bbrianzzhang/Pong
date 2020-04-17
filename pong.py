import turtle

wn = turtle.Screen()
wn.title("Pong time")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

Score_A = 0
Score_B = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align = "center", font=("Courier", 24, "normal"))

def paddle_a_up():
    if paddle_a.ycor() >= 250:
        paddle_a.sety(250)
    else:
        paddle_a.sety(paddle_a.ycor()+10)


def paddle_a_down():
    if paddle_a.ycor() <= -250:
        paddle_a.sety(-250)
    else:
        paddle_a.sety(paddle_a.ycor()-10)


def paddle_b_up():
    if paddle_b.ycor() >= 250:
        paddle_b.sety(250)
    else:
        paddle_b.sety(paddle_b.ycor()+10)


def paddle_b_down():
    if paddle_b.ycor() <= -250:
        paddle_b.sety(-250)
    else:
        paddle_b.sety(paddle_b.ycor()-10)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        Score_A += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(Score_A, Score_B), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        Score_B += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(Score_A, Score_B), align="center", font=("Courier", 24, "normal"))

    if 340 < ball.xcor() < 350 and paddle_b.ycor() + 60 > ball.ycor() > paddle_b.ycor() - 60:
        ball.setx(340)
        ball.dx *= -1

    if -340 > ball.xcor() > -350 and paddle_a.ycor() + 60 > ball.ycor() > paddle_a.ycor() - 60:
        ball.setx(-340)
        ball.dx *= -1
