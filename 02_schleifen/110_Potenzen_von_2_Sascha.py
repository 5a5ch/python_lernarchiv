# Potenzen von zwei
#
# Schreibe ein Programm, das alle Potenzen von 2 ausgibt
# deren Ergebnis kleiner als 10.000 ist.
# Hilfsmittel: Schleife, **
#
# Zusatz: Die Ausgabe soll folgendermaßen aussehen:
# 2 ** 0 = 1
# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8
# 2 ** 4 = 16
# 2 ** 5 = 32
# 2 ** 6 = 64
# ...

y = 0

while True:
    x = 2**y
    if x >= 10000:
        break
    print(f'2 ** {y} = {x}', end='   ')
    y=y+1
    print()
