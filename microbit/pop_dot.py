from microbit import *
import random

dot_x = 0
dot_y = 2
points = 0
lives = 5

while True:
    display.set_pixel(dot_x, dot_y, 0)
    dot_x = dot_x + 1
    dot_y = random.randint(0,4)
    display.set_pixel(dot_x, dot_y, 9)
    sleep(500)
    if button_a.is_pressed() and dot_x == 2:
        display.show(Image.HAPPY)
        points = points + 1
        dot_x = 0
        sleep(500)
        display.clear()
    if dot_x >= 4:
        lives = lives - 1
        display.show(Image.SAD)
        dot_x = 0
        sleep(500)
        display.clear()
    if points >= 5:
        display.scroll("YOU WIN")
        break
    if lives <= 0:
        display.scroll("RIP")
        break