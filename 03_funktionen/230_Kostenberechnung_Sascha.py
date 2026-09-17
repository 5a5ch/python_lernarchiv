
# Kostenberechnung

"""
Erstelle eine Funktion zur Kostenberechnung.
Dieser wird Preis, Anzahl und Währung als Argumente übergeben
und sie soll daraus die Kosten berechnen und zurückgeben.
Standardmäßig soll die Anzahl 100 betragen
und die Währung Euro sein.

Teste die Funktion:
print(berechne_kosten(2))  # 200 €
print(berechne_kosten(2, 2))  # 4 €
print(berechne_kosten(2, 2, '$'))  # 4 $
print(berechne_kosten(2, waehrung='$'))  # 200 $
"""


def kosten_berechnen(preis, anzahl=100, währung='€'):
    if währung == '€':
        umrechnung_währung = 1
    if währung == '$':
        umrechnung_währung = 1.16
    if währung == 'Yen':
        umrechnung_währung = 185.48
    if währung == 'Yuan':
        umrechnung_währung = 7.83
    kosten = round(preis * anzahl * umrechnung_währung,2)
    ausgabe = [kosten, währung]
    return ausgabe

# zum Testen
liste_preis = [1,1.99,1699,25000]
liste_anzahl = [100,500,5,2]
liste_währung = ['€','$','Yen','Yuan']


x = 0
for _ in range(len(liste_preis)):
    liste_ausgabe = kosten_berechnen(liste_preis[x], liste_anzahl[x], liste_währung[x])
    print(f'Die Kosten betragen {liste_ausgabe[0]} {liste_ausgabe[1]}')
    x += 1
