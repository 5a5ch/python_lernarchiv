# Fakultät

"""
Schreibe ein Skript, dass ermittelt,
welche Zahl möglichst groß ist,
ohne dass ihre Fakultät über 1.000.000.000 ist.

Hinweis:
Fakultät von 5 (Kurzschreibweise: 5!):
1 * 2 * 3 * 4 * 5 = 120
"""

listefak = []              # leere Liste

print(listefak)

import math                # für die Fakultät-Funktion

lim = 1000000000           # Grenzwert
n = 1                      # Startwert zum testen

fak = math.factorial(n)

while fak < lim:
    fak = math.factorial(n)
    print(fak)
    listefak.append(fak)
    n += 1

print(listefak)

max = listefak.pop()

print(f'der höchste Wert <= {lim} ist {max}')