import turtle

lea = turtle.Turtle()

lea.penup()
lea.goto(0, -200)

lea.pendown()
lea.circle(200)

lea.penup()
lea.goto(0,0)
lea.pendown()
for i in range(100):
	lea.circle(100)
	lea.left(10)

a = input()


