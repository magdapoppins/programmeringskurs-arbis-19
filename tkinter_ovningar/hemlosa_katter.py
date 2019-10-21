from tkinter import Tk, Button, simpledialog

root = Tk()
root.title("Hemlösa katter")
root.resizable(width=False, height=False)

class Cat:
	def __init__(self, name, age):
		self.name = name
		self.age = age

misse = Cat("Misse", 3)
print(misse)

kissing_cat = u'\u1F63D'

while True:
	#cat_name = simpledialog.askstring("Ny katt", "Vad heter katten?")

root.mainloop()