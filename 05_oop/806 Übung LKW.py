# Hier ist der aus dem Bild ausgelesene Text:
#
# # Aufgabe 2: Fahrzeug-Eigenschaften erweitern
#
# **Szenario:** Ein Fuhrparkunternehmen verwaltet verschiedene Fahrzeuge. Alle Fahrzeuge besitzen eine Marke. Lastkraftwagen (Lkw)
# besitzen zusätzlich eine Angabe zur Ladekapazität.
#
# ## Arbeitsauftrag:
#
# 1. Eine Basisklasse `Fahrzeug` mit dem Attribut `marke` definieren.
#
# 2. Eine abgeleitete Klasse `Lkw` erstellen, die von `Fahrzeug` erbt.
#
# 3. Die Klasse `Lkw` mit einem eigenen Konstruktor ausstatten. Dieser soll die `marke` sowie das neue Attribut `ladekapazitaet`
# (in Tonnen) entgegennehmen und speichern.
#
# 4. Eine Methode `info(self)` in der Klasse `Lkw` erstellen, welche die Marke und die Ladekapazität auf der Konsole ausgibt.


class Fahrzeug:
    def __init__(self, p_marke):
        self.marke = p_marke

class LKW(Fahrzeug):
    def __init__(self, p_marke, p_ladekapazitaet):
        super().__init__(p_marke)
        self.ladekapazitaet = p_ladekapazitaet
    def info(self):
        print(f'Marke: {self.marke} \nLadekapazität: {self.ladekapazitaet}')

lkw1 = LKW('Scania', 12.7)
lkw1.info()
