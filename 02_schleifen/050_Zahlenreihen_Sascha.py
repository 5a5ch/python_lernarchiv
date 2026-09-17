# Zahlenreihen

# Schaue, welche der 12 Aufgaben du schon lösen kannst.
# Je mehr, desto besser, aber es müssen nicht alle sein.


# 1. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5

print('Schleife 1')

schleife1 = range(1,6)
print(list(schleife1))

for schleife1_1 in range(1,6):
    print(schleife1_1, end='  ')

print()
print()


# 2. Schreibe eine Schleife, die Folgendes ausgibt:
# 100 90 80 70 60 50 40 30 20 10

print('Schleife 2')

schleife2 = range(100,9,-10)
print(list(schleife2))

for schleife2_1 in range(100,9,-10):
    print(schleife2_1, end='  ')

print()
print()


# 3. Schreibe eine Schleife, die Folgendes ausgibt:
# 2000 3000 4000 5000 6000

print('Schleife 3')

# erster Versuch:
# schleife3 = range(200,6001,1000)
# print(list(schleife3))

# Lösung
schleife3 = range(2000,6001,1000)
print(list(schleife3))

for schleife3_1 in range(2000,6001,1000):
    print(schleife3_1, end='   ')

print()
print()


# 4. Schreibe eine Schleife, die Folgendes ausgibt:
# 13 17 21 25 29

print('Schleife 4')

schleife4 = range(13,30,4)
print(list(schleife4))

for schleife4_1 in range(13,30,4):
    print(schleife4_1, end='   ')

print()
print()


# 5. Schreibe eine Schleife, die Folgendes ausgibt:
# 2.0 1.5 1.0 0.5 0.0 -0.5 -1.0

print('Schleife 5')

# Test:
# zuerst ganze Zahlen erzeugen
# schleife5 = range(4,-3,-1)
# print(list(schleife5))

for schleife5_1 in range(4,-3,-1):
    print(schleife5_1 / 2, end='   ')

print()
print()


# 6. Schreibe eine Schleife, die Folgendes ausgibt:
# 1.0 2.2 3.4 4.6 5.8 7.0 8.2 9.4

for schleife6 in range(10,95,12):
    print(schleife6 / 10, end='   ')

print()
print()


# 7. Schreibe eine Schleife, die Folgendes ausgibt:
# Beachte: die 7 fehlt!
# 1 2 3 4 5 6 8 9 10

print('Schleife 7')

for schleife7 in range(1,7):
    print(schleife7, end='   ')

for schleife7_1 in range(8,11):
    print(schleife7_1, end='   ')

print()
print()

# Versuch:
# Die Ausgabe direkt in einem f-String zu erzeugen.
# Funktioniert so nicht.

# print(f'Schleife 7 v02\n'{for schleife75 in range(1,7): print(schleife75, end='   ')})


# 8. Schreibe eine Schleife, die Folgendes ausgibt:
# Beachte: die 25 und die 41 fehlen!
# 13 17 21 29 33 37 45

print('Schleife 8')

# erster Einsatz von continue
# damit werden die Werte 25 und 41 übersprungen

for schleife8 in range(13,46,4):

    if schleife8 == 25:
        continue

    if schleife8 == 41:
        continue

    print(schleife8,end='   ')

print()
print()


# 9. Schreibe eine Schleife, die Folgendes ausgibt:
# Z5 Z7 Z9 Z11 Z13

print('Schleife 9')

for schleife9 in range(5,14,2):
    print('Z', end='')
    print(schleife9,end='   ')

print()
print()


# 10. Schreibe eine Schleife, die Folgendes ausgibt:
# a2b3 a12b13 a22b23

print('Schleife 10')

for schleife10_1 in range(2,23,10):
    print('a',end='')
    print(schleife10_1,end='')
    print('b',end='')
    print(schleife10_1 + 1,end='   ')

print()
print()


# 11. Schreibe eine Schleife,
# die alle Zahlen von 1 bis 20 addiert
# und danach das Endergebnis ausgibt.

print('Schleife 11')         # Überschrift

schleife11 = range(1,21)     # Zahlenbereich erstellen
print(list(schleife11))      # Liste ausgeben

Ergebnis = sum(schleife11)   # sum Befehl zum Summieren der Liste

print(Ergebnis)

print()
print()


# 12. Schreibe EINE Schleife, die Folgendes ausgibt:
# 1 2 3 4 5 4 3 2 1

print('Schleife 12')

for schleife12 in range(1,10):

    if schleife12 <= 5:
        print(schleife12,end='   ')

    if schleife12 == 6:
        print('4', end='   ')

    if schleife12 == 7:
        print('3', end='   ')

    if schleife12 == 8:
        print('2', end='   ')

    if schleife12 == 9:
        print('1', end='   ')