
# Zahl raten

"""
Schreibe ein Programm, das sich eine Zahl ausdenkt
und den Benutzer diese Zahl raten lässt.
Nach jedem Versuch soll das Programm ausgeben,
ob zu hoch, zu niedrig oder richtig geraten wurde.
"""


from random import randint

zahl = randint(1,10)

for _ in range(10):
    guess = int(input(f'Rate welche Zahl sich das Programm ausgedacht hat. Du hast 10 Versuche\n'))
    if guess < zahl:
        print('Die gesuchte Zahl ist größer.')
    if guess > zahl:
        print('Die gesuchte Zahl ist kleiner.')
    if guess == zahl:
        print('Erraten!!!')
        break