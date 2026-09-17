
# Honky-Tonk

# Simuliere das Spiel Honky-Tonk.
# Bei diesem Spiel bezahlt der Spieler pro Runde einen Euro als Einsatz.
# Er darf nun drei Würfel werfen.
# Zeigt mindestens ein Würfel eine sechs,
# so erhält er zunächst den Einsatz zurück.
# Zudem erhält er für jede geworfene Sechs zusätzlich
# einen Euro als Gewinn ausbezahlt.
# Liegt keine Sechs, so verliert er den Einsatz.
# Starte mit einem Kapital von 1000 Euro und simuliere 1000 Runden.

kapital = 1000
einsatz = 1
zwischenstand = []

from random import randint



#print(f'Alea iacta est: {wuerfel1}, {wuerfel2}, {wuerfel3}')
# Version 1 - mit falschen Ergebnissen.

for _ in range(1000):
    kapital = kapital - einsatz
    wuerfel1 = randint(1, 6)
    wuerfel2 = randint(1, 6)
    wuerfel3 = randint(1, 6)
    if wuerfel1 == 6 or wuerfel2 == 6 or wuerfel3 == 6:
        kapital = kapital + 2
        if wuerfel1 == wuerfel2 == 6:
            kapital = kapital + 1
        if wuerfel1 == wuerfel3 == 6:
            kapital = kapital + 1
        if wuerfel2 == wuerfel3 == 6:
            kapital = kapital + 1
    zwischenstand.append(kapital)

print(zwischenstand)



