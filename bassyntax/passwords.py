import random

adjektiivit = ['vihreä', 'kateellinen', 'huikea', 'herkullinen', 'vuotava']
substantiivit = ['auto', 'nakki', 'hirvi', 'läppäri', 'ystävä']
merkit = ['@', '!', '?', '-.-', ':D', '><']

salasana = random.choice(adjektiivit) + \
    random.choice(substantiivit) + random.choice(merkit)

print(salasana)
