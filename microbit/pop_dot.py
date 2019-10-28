from microbit import *

dot_x = 0
dot_y = 3

while True:
    sleep(2000)
    microbit.display.set_pixel(dot_x, dot_y, 9)
    dot_x = dot_x + 1
    if button_a.is_pressed() and dot_x == 3:
        display.show(Image.HAPPY)
        sleep(5000)
        break
