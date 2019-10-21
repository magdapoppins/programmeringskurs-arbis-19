class Hund:
    def __init__(self, snack, name):
        self.snack = snack
        self.name = name

    # def __repr__(self):
        # return self.name

    def bark(self):
        print("WOFF")


voffe = Hund("köttbullar", "Voffe")
pluto = Hund("morot", "Pluto")

voffe.bark()
print(voffe)
print(voffe.snack)
