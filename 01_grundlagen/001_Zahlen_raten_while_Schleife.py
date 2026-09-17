# Zahlen raten

from random import randint

zahl = randint(1, 200)   # Computer generiert eine zufällige Zahl

guess = int(input('Rate welche zufällige Zahl zw. 1-200 der Computer gewählt hat.\n'))

while zahl != guess:

    if guess < zahl:
        print('zu niedrig')

    if guess > zahl:
        print('zu hoch')

    guess = int(input('Rate welche zufällige Zahl zw. 1-200 der Computer gewählt hat.\n'))

print('Richtig:', zahl)