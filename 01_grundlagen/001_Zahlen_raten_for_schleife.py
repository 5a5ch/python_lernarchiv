# Zahlen raten

from random import randint

zahl = randint(1, 200)   # Computer generiert eine zufällige Zahl

# Schleife mit 10 Wiederholungen zum Raten.
for i in range(1, 10):
    guess = int(input('Rate welche zufällige Zahl zw. 1-200 der Computer gewählt hat.\n'))

    if guess == zahl:
        print('Richtig:', end=' ')
        break

    if guess < zahl:
        print('zu niedrig')

    if guess > zahl:
        print('zu hoch')

print(zahl)