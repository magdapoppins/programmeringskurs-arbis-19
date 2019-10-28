from microbit import *
import random

def flip_coin():
    result = random.randint(0, 1)
    if result == 0:
        return Image.HAPPY
    else:
        return Image.SAD


while True:
    if button_a.is_pressed():
        display.show(result)
    elif button_b.is_pressed():
        break
    else:
        display.show("?")
        result = flip_coin()

display.clear()