
# Doppelte Zahl

"""
Schreibe eine Funktion, die überprüft,
ob in einer Liste mit Zahlen zwei Zahlen gleich sind.
Der Funktion wird die Liste übergeben
und sie soll True zurückgeben, wenn es doppelte Zahlen gibt
und ansonsten soll die Funktion False zurückgeben.
"""

from random import randint

liste = [1,7,5,9,0,0]   # Listeninhalt


liste.sort()
print(liste)
print('Es wird geprüft ob die obige Liste doppelte Zahlen enthält.')
print('Falls ja, wird True ausgegeben, falls nein False.')
print()
x = len(liste)
#print(f'Länge der Liste {x}')
#a = x - x
#b = x - x + 1
#z = (x - 1) - (x - 2)

def dopzahl(liste):
    a = x - x                      # Listenposition A
    b = x - x + 1                  # Listenposition B
    z = (x - 1) - (x - 2)          # counter
    for _ in range(x-1):           # vergleichen der Werte
        if liste[a] == liste[b]:
            erg_true = liste[a] == liste[b]
            return(erg_true)
            break
        if z == x - 1:
            erg_false = liste[a] == liste[b]
            return(erg_false)
        a += 1
        b += 1
        z += 1

print(f'Ergebnis: {dopzahl(liste)}')