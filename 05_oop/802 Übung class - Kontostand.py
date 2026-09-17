# Aufgabe 3: Erstelle eine Klasse 'Konto' mit dem Attribut kontostand und einer Methode einzahlen(betrag) und
# auszahlen(betrag) . Der Betrag soll entspreched geändert werden.

class Konto:
    def __init__(self, p_kontostand):
        self.kontostand = p_kontostand

    def einzahlen(self, wert):
        self.kontostand = self.kontostand + wert
        print(f'Sie haben {wert} € eingezahlt. Neuer Kontostand: {self.kontostand} €')

    def auszahlen(self, wert):
        self.kontostand = self.kontostand - wert
        print(f'Sie haben {wert} € abgehoben. Neuer Kontostand: {self.kontostand} €')

konto1 = Konto(1000)
print(f'Ihr Kontostand beträgt: {konto1.kontostand} €')
konto1.einzahlen(150)
konto1.auszahlen(75)
print(f'Ihr Kontostand beträgt: {konto1.kontostand} €')
