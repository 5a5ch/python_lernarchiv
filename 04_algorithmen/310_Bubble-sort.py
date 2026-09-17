
# Bubblesort

"""
Schreibe eine Funktion,
der man eine Liste mit beliebig vielen Zahlen als Werten übergeben kann
und die diese Liste sortiert und zurückgibt.

Benutze hierzu den Bubblesort-Algorithmus.
Bei diesem wird die Liste durchlaufen
und jede Zahl mit der jeweils nachfolgenden Zahl verglichen.
Wenn die nachfolgende Zahl kleiner ist,
werden die Zahlen getauscht.
Die Liste wird so lange durchlaufen,
bis bei einem Durchlauf keine Zahlen getauscht werden müssen.
"""
from random import randint
liste = []
for _ in range(15):
    x = randint(0, 1000)
    liste.append(x)



def listesortieren(liste):
    for _ in range(len(liste)-1):
        x = 0
        y = 1
        for _ in range(len(liste)-1):
            if liste[x] >= liste[y]:
                liste[x], liste[y] = liste[y], liste[x]
                # print(liste[x], liste[y])
            x += 1
            y += 1
    return liste


print(listesortieren(liste))