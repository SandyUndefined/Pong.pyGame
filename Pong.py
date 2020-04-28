import turtle
wn = turtle.Screen()
wn.title("Ping Pong @Sandy_undefined")
wn.bgcolor("#ff9933")
wn.setup(width=800,height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#Bar 1
bar_a = turtle.Turtle()
bar_a.speed(1)
bar_a.shape("square")
bar_a.shapesize(stretch_wid=5,stretch_len=1)
bar_a.color("black")
bar_a.penup()
bar_a.goto(-350,0)


#Bar 2
bar_b = turtle.Turtle()
bar_b.speed(1)
bar_b.shape("square")
bar_b.shapesize(stretch_wid=5,stretch_len=1)
bar_b.color("black")
bar_b.penup()
bar_b.goto(350,0)

#Pong
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = .5
ball.dy = .5

#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier",24,"bold"))

#Funtions
def bar_a_up():
    y = bar_a.ycor()
    y += 20
    bar_a.sety(y)

def bar_a_down():
    y = bar_a.ycor()
    y -= 20
    bar_a.sety(y)

def bar_b_left():
    y = bar_b.ycor()
    y += 20
    bar_b.sety(y)

def bar_b_right():
    y = bar_b.ycor()
    y -= 20
    bar_b.sety(y)



# Keyborad binding

wn.listen()
wn.onkeypress(bar_a_up,"w")
wn.onkeypress(bar_a_down,"s")
wn.onkeypress(bar_b_left,"Up")
wn.onkeypress(bar_b_right,"Down")

while True:
    wn.update()

    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if bar_a.ycor() > 240:
        bar_a.sety(240)

    if bar_a.ycor() < -240:
        bar_a.sety(-240)

    if bar_b.ycor() > 240:
        bar_b.sety(240)

    if bar_b.ycor() < -240:
        bar_b.sety(-240)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-.8

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-.8

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx*=-.8
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx*=-.8
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    #Collisions
    if (ball.xcor() >340 and ball.xcor() <350) and (ball.ycor() < bar_b.ycor() +40 and ball.ycor() > bar_b.ycor()-40):
        ball.setx(340)
        ball.dx *=-.8
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bar_a.ycor() +40 and ball.ycor() > bar_a.ycor()-40):
        ball.setx(-340)
        ball.dx *=-.8

