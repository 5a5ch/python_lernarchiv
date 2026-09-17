
# Nettopreis

"""
Schreibe eine Funktion zum Berechnen des Nettopreises.
Dieser Funktion soll der Bruttopreis übergeben werden
und sie soll den Nettopreis zurückgeben.
Der Mehrwertsteuersatz soll als zweiter Parameter
übergeben werden können.
Der Standardwert des Mehrwertsteuersatzes soll 19 sein.

Teste die Funktion:
print(berechne_netto(119))     # 100.0
print(berechne_netto(107, 7))  # 100.0
"""


def netto_rechner(brutto, ust = 19):
    netto = brutto / (ust/100+1)
    return netto

# zum Testen
liste_brutto = [119,238,74.9, 321]
liste_ust = [19,19,7,7]

x = 0
for _ in range(len(liste_brutto)):
    print(netto_rechner(liste_brutto[x], liste_ust[x]))
    x += 1

