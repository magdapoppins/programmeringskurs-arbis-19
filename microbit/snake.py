from microbit import *
import random

snack_x = 0
snack_y = 0
points = 0
speed = 1000

while True:
    display.set_pixel(snack_x, snack_y, 0)
    snack_x, snack_y = random.randint(0, 4), random.randint(0, 4)
    display.set_pixel(snack_x, snack_y, 9)
    sleep(speed)
    if button_a.was_pressed() and (snack_x == 2 or snack_y == 2):
        points = points + 1
    if points >= 3:
        display.show(Image.HAPPY)
        sleep(500)
        display.clear()
        speed = speed - 100