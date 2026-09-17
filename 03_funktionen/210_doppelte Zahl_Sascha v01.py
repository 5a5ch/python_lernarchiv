
# Doppelte Zahl

"""
Schreibe eine Funktion, die überprüft,
ob in einer Liste mit Zahlen zwei Zahlen gleich sind.
Der Funktion wird die Liste übergeben
und sie soll True zurückgeben, wenn es doppelte Zahlen gibt
und ansonsten soll die Funktion False zurückgeben.
"""

from random import randint
liste = [1,7,5,9,0,0]
liste.sort()
print(liste)
x = len(liste)
print(f'Länge der Liste {x}')
a = x - x
b = x - x + 1
z = (x - 1) - (x - 2)


for _ in range(x-1):
    if liste[a] == liste[b]:
        erg_true = liste[a] == liste[b]
        print(erg_true)
        break
    if z == x - 1:
        print(liste[a] == liste[b])
    a += 1
    b += 1
    z += 1