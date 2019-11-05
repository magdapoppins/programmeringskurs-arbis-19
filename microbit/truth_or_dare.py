from microbit import *
import random

truths = [
    'Mita sina pelkaat?',
    'Noloin asia mitä sinulle on sattunut?',
    'Mika on suurin unelmasi?'
]

dares = [
    'Mene ulos ilman takkia ja laske 10:n',
    'Tee hassu ilme',
    'Laita kaikkien kengät jarjestykseen.'
]

while True:
    display.scroll("Totuus (A) vai tehtava (B)?")
    if button_a.was_pressed():
        display.scroll(random.choice(truths))
        sleep(5000)
    elif button_b.was_pressed():
        display.scroll(random.choice(truths))
        sleep(5000)