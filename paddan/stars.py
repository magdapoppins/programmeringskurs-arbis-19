import turtle
import random

dunder = turtle.Turtle()
dunder_himmel = turtle.Screen()
dunder_himmel.bgcolor("black")

def rita_stjarna():
	x = random.randint(-200, 200)
	y = random.randint(-200, 200)	
	dunder.penup()
	dunder.goto(x, y)
	dunder.color("yellow")
	dunder.begin_fill()
	dunder.pendown()
	for i in range(5):
		dunder.forward(30)
		dunder.left(145)
	dunder.end_fill()


rita_stjarna()


for i in range(100):
	rita_stjarna()
