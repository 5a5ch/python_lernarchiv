
# Teilersumme

"""
Schreibe eine Funktion, die überprüft, ob bei einer Zahl
die Summe aller Teiler kleiner als die Zahl ist.
Die Zahl selber soll hierbei nicht zu den Teilern zählen.

Bei 81 würde True zurückgegeben werden, da
1 + 3 + 9 + 27 = 40
und 40 < 81

Bei 80 würde False zurückgegeben werden, da
1 + 2 + 4 + 5 + 8 + 10 + 16 + 20 + 40 = 106
und 106 > 80
"""

# 20/1=20   20/2=10   20/4=5   20/5=4   20/10=2
#teilerliste = []
#zahl = 80
#n = 1        # Zähler

print('True = Summe aller Teiler kleiner als die Zahl\nFalse = Summe aller Teiler größer als die Zahl')
print()
def teilersumme(zahl):
    teilerliste = []
    n = 1
    while n < zahl:
        check = zahl%n    # Modulo = 0 -> Ganzzahl
        if check == 0:
            teilerliste.append(n)     # bei Ganzzahl hinzufügen zur Liste
        n += 1                    # Zähler erhöhen
    print(f'Teilerliste: {teilerliste}')
    print(f'Summe der Teilerliste: {sum(teilerliste)}')
    #print(sum(teilerliste) < zahl)
    return(sum(teilerliste) < zahl)

print(teilersumme(int(input('Gib eine Zahl ein\n'))))
