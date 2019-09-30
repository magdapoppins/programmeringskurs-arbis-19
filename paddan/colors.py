import turtle

jenny = turtle.Turtle()

rainbow = ["green", "yellow", "hotpink"]

for color in rainbow:
	jenny.begin_fill()
	jenny.color(color)
	jenny.circle(50)
	jenny.left(30)
	jenny.end_fill()

a = input()