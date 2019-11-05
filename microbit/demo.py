from microbit import *
import random

totuudet = [
    'Suurin pelkosi?',
    'Huonoin arvosana?'
]

tehtavat = [
    'Jarjestele kaikkien kengat!',
    'Silita kaktusta!'
]

while True:
    display.scroll("Totuus (A) vai tehtava (B)?")
    if button_a.was_pressed():
        display.scroll(random.choice(totuudet))
    if button_b.was_pressed():
        display.scroll(random.choice(tehtavat))

