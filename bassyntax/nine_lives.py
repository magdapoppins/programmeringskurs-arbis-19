import random

heart = u'\u1F496'
lives_count = 9
words = ['pasta', 'mango', 'penna', 'glass', 'fågel']
clue = ['?', '?', '?', '?', '?']
secret_word = random.choice(words)
guessed_correct = False

def update_clue(guessed_character, secret_word, clue):
    for i in range(len(secret_word)):
        if secret_word[i] == guessed_character:
            clue[i] = guessed_character

while lives_count > 0:
    print(clue)
    print("Liv kvar: " + heart * lives_count)
    guess = input("Gissa en bokstav eller hela ordet!   ")

    if guess == secret_word:
        guessed_correct = True
        break
    
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print("Du förlorade ett liv!")
        lives_count -= 1

if guessed_correct:
    print("DU VANN! Det hemliga ordet var " + secret_word)
else:
    print("Du förlorade, order var " + secret_word)
