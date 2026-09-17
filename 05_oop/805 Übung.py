# Aufgabe 1: Die Haustier-Basis
# Szenario: Ein Tierheim benötigt eine Software zur Verwaltung von Tieren. Jedes Tier besitzt einen Namen.
# Arbeitsauftrag:
#
# Eine Basisklasse Tier erstellen. Der Konstruktor (__init__) soll das Attribut name initialisieren.
#
# Eine Methode vorstellen(self) in der Klasse Tier implementieren. Die Ausgabe soll lauten:
# "Ich bin ein Tier und heiße [Name]."
#
# Eine abgeleitete Klasse Hund erstellen, die von Tier erbt. Diese Klasse bleibt zunächst ohne eigene Attribute oder Methoden
# (Schlüsselwort pass verwenden).
#
# Ein Objekt der Klasse Hund mit dem Namen "Bello" instanziieren und die geerbte Methode vorstellen() aufrufen.


class Tier:
    def __init__(self, p_name):
        self.name = p_name

    def vorstellen(self):
        print(f'Ich bin ein Tier und heiße {self.name}.')

tier1 = Tier('Bobo')
tier1.vorstellen()

class Hund(Tier):
    pass

hund1 = Hund('Bello')
hund1.vorstellen()