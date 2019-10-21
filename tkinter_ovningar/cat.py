class Cat:
	def __init__(self, name, age):
		self.name = name
		self.age = age

majkens_namn = input("Vad heter katten?")
majkens_alder = int(input(f"Hur gammal är {majkens_namn}?"))

majken = Cat(majkens_namn, majkens_alder)
print(majken.name, majken.age)
