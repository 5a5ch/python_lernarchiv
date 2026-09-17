# Korrektes Datum

"""
Die Meyer GmbH benötigt ein Modul,
das ein beliebiges Datum auf Korrektheit prüft.

Ist das zu prüfende Datum korrekt,
so ist die Variable datok auf 1, andernfalls auf 0
zu setzen.

Beispiele:

29.02.1999 - datok: 0
29.02.2000 - datok: 1
13.05.2000 - datok: 1
32.05.2000 - datok: 0
24.13.2000 - datok: 0

Für die Jahre gilt: jahr > 1900 UND jahr < 2100
"""

# Eingabe Jahr

y = int(input('Gib eine Jahreszahl zwischen 1900 und 2100.\n'))

while y < 1900 or y > 2100:
    y = int(input('Junge, erst lesen, dann eingeben: Jahreszahl zwischen 1900 und 2100.\n'))

check = y % 4    # Prüfung ob Schaltjahr - Modulo muss 0 ergeben


# Eingabe Monat

m = int(input('Gib den Monat an. Zur Erinnerung: Zahl von 1 bis 12.\n'))

while m < 1 or m > 12:
    m = int(input('Ufff, nochmal langsam für dich: Zahl von 1 bis 12\n'))


# Eingabe Tag

d = int(input('Gib den Tag ein. (Zahl von 1 bis 31)\n'))

while d < 1 or d > 31:
    d = int(input('Bedenke der Monat hat nie mehr als 31 Tage, Guybrush!\n'))

while (m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
    d = int(input('Oops, jetzt is was schief gelaufen. Gib den Tag nochmal ein. (Zahl von 1 bis 30)\n'))

while m == 2 and d > 29:
    d = int(input('Junge, so langsam wird s aber verdächtig. (Zahl von 1 bis 29\n'))

while m == 2 and d == 29 and check != 0:
    d = int(input('Nich jedes Jahr is n Schaltjahr, du Deckel! (Zahl von 1 bis 28\n'))

print(f'Das eingegebene Datum {d:02}.{m:02}.{y} hat (endlich) ein korrektes Format')


# or 6 or 9 or 11

# Ausgabe
# print(f'Das eingegebene Datum {d:02}.{m:02}.{y} hat ein korrektes Format')