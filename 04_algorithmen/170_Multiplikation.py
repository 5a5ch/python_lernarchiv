
# Multiplikation

# Schreibe ein Programm, das ermittelt,
# wie viele ganzzahlige Multiplikator-Multiplikand-Kombinationen
# vom Produkt 8.420.000 es gibt,
# bei denen sowohl Multiplikator als auch Multiplikand
# kleiner als 10.000 sind.
#
# 1000 * 8420 und 8420 * 1000 zählt nur einmal.

# Gib die Zahlenpaare aus:
# 1000 * 8420
# 1250 * 6736
# ...


liste_x = []   # hier werden der erste Multiplikant eingetragen, wenn Ganzzahl
liste_y = []   # hier wird der zweite Multiplikant eingetragen, wenn Ganzzahl

x = 1  # Startwert
y = 2  # Startwert, damit die Schleife läuft (wird mit Beginn neu definiert)

# Berechnung der Kombinationen und Eintrag in die jeweilige Liste
while x < y:
      y = 8420000 / x
      z = y%1
      if z == 0:
          liste_x.append(int(x))
          liste_y.append(int(y))
      x += 1


# Länge der Liste und Variable für Schleife
a = len(liste_x)
a2 = a
b = len(liste_y)
b2 = b

# Schleife für die Ausgabe der Kombinationen
for _ in range(len(liste_x)):
    print(f'{liste_x[a-a2]} * {liste_y[b-b2]}')
    a2 -= 1
    b2 -= 1

# Ausgabe Anzahl Kombinationen
print(f'es gibt {len(liste_x)} Kombinationen')