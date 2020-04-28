import turtle
wn = turtle.Screen()
wn.title("Ping Pong @Sandy_undefined")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Bar 1
bar_a = turtle.Turtle()
bar_a.speed(1)
bar_a.shape("square")
bar_a.shapesize(stretch_wid=.8,stretch_len=8)
bar_a.color("white")
bar_a.penup()
bar_a.goto(0,250)


#Bar 2
bar_b = turtle.Turtle()
bar_b.speed(1)
bar_b.shape("square")
bar_b.shapesize(stretch_wid=.8,stretch_len=8)
bar_b.color("white")
bar_b.penup()
bar_b.goto(0,-250)

#Pong
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(stretch_wid=1.5,stretch_len=1.5)
ball.penup()
ball.goto(0,0)
ball.dx = .5
ball.dy = .5

#Funtions
def bar_a_left():
    x = bar_a.xcor()
    x -= 20
    bar_a.setx(x)

def bar_a_right():
    x = bar_a.xcor()
    x += 20
    bar_a.setx(x)

def bar_b_left():
    x = bar_b.xcor()
    x -= 20
    bar_b.setx(x)

def bar_b_right():
    x = bar_b.xcor()
    x += 20
    bar_b.setx(x)



# Keyborad binding

wn.listen()
wn.onkeypress(bar_a_left,"a")
wn.onkeypress(bar_a_right,"d")
wn.onkeypress(bar_b_left,"Left")
wn.onkeypress(bar_b_right,"Right")

while True:
    wn.update()

    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx*=-1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx*=-1

    #Collisions
    if ball.xcor() > 250  and (ball.ycor() < bar_a.xcor()+ 50 and ball.ycor() > bar_a.ycor()-50):
