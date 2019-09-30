import turtle

sissi = turtle.Turtle()

def rektangel(h, w, color):
	sissi.color(color)
	sissi.begin_fill()
	for i in range(4):
		if i % 2 is 0:
			sissi.forward(w)
		else: 
			sissi.forward(h)
		sissi.left(90)
	sissi.end_fill()

rektangel(100, 50, "green")