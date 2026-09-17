# Kleines Einmaleins

"""
Schreibe ein Programm,
welches das kleine Einmaleins formatiert ausgibt:

001 002 003 004 005 006 007 008 009 010
002 004 006 008 010 012 014 016 018 020
...
010 020 030 040 050 060 070 080 090 100
"""

print('Aufgabe: Schreibe ein Programm, welches das kleine Einmaleins formatiert ausgibt.')
print('Mit welcher Zahl möchtest du beginnen?')


# -----------------------------
# Version 2 (endgültige Lösung)
# -----------------------------

print()

x = int(input())

for i in range(1,11):
    for j in range(1,11):
        print(f'{j * x:03}', end='   ')
    x = x + 1
    print()


# -----------------------------
# Version 1 (erster Lösungsansatz)
# -----------------------------
#
# Die erste Lösung entstand noch ohne verschachtelte Schleifen.
# Dabei wurde jede Zeile des Einmaleins einzeln programmiert.
# Die Lösung funktioniert, wurde aber später durch Version 2 ersetzt.
#
# for einser in range(1,11):
#     if 0 <= einser < 10:
#         print('00',end='')
#     if 9 < einser < 100:
#         print('0',end='')
#     print(einser,end='   ')
# print()
#
# for zweier in range(1,11):
#     zweier2 = zweier * 2
#     if 0 <= zweier2 < 10:
#         print('00',end='')
#     if 9 < zweier2 < 100:
#         print('0',end='')
#     print(zweier2,end='   ')
# print()
#
# ...
#
# for zehner in range(1,11):
#     zehner2 = zehner * 10
#     if 0 <= zehner2 < 10:
#         print('00',end='')
#     if 9 < zehner2 < 100