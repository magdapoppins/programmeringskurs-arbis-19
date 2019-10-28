from microbit import *
import random

answers = [
    "Kyllä",
    "Ei"
]

while True:
    display.show('?')
    if accelerometer.was_gesture('shake'):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))
    sleep(10)