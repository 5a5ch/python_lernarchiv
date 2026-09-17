# # Aufgabe 2: Berechnungen im Fuhrpark
#
# **Szenario:** Ein Fuhrparkunternehmen möchte die Reichweite von Fahrzeugen berechnen. Ein Standard-Fahrzeug hat eine feste
# Reichweite basierend auf dem Tankinhalt. Bei einem Lastkraftwagen (Lkw) verringert sich die Reichweite aufgrund des Gewichts
# der Ladung.
#
# ## Arbeitsauftrag:
#
# 1. Eine Basisklasse `Fahrzeug` mit den Attributen `marke` und `tankinhalt` (in Litern) erstellen.
# 2. In `Fahrzeug` eine Methode `berechne_reichweite(self)` implementieren. Die Formel lautet:
#
#    ```python
#    tankinhalt * 10
#    ```
#
#    Die Methode soll die berechnete Reichweite als Zahl zurückgeben (`return`).

# 3. Eine abgeleitete Klasse `SchwererLkw` erstellen, die von `Fahrzeug` erbt. Der Konstruktor soll zusätzlich das Attribut
# `ladung_tonnen` initialisieren.
# 4. Die Methode `berechne_reichweite(self)` in der Klasse `SchwererLkw` so überschreiben, dass von der Standard-Reichweite pro
# Tonne Ladung 50 Kilometer abgezogen werden. Formel:
#    ```python
#    (tankinhalt * 10) - (ladung_tonnen * 50)
#    ```
# 5. Ein Objekt der Klasse `SchwererLkw` erstellen (z. B. 100 Liter Tank, 2 Tonnen Ladung). Die Methode aufrufen und das Ergebnis
# ausgeben.


class Fahrzeug:
    def __init__(self, p_marke, p_tankinhalt):
        self.marke = p_marke
        self.tankinhalt = p_tankinhalt
        self.reichweite = 0
    def reichweite_berechnen(self):
        self.reichweite = self.tankinhalt * 10
        return self.reichweite

class schwererLKW(Fahrzeug):
    def __init__(self, p_marke, p_tankinhalt, p_zuladung):
        super().__init__(p_marke, p_tankinhalt)
        self.zuladung = p_zuladung
    def reichweite_berechnen(self):
        ergebnis = super().reichweite_berechnen()
        #self.reichweite = self.tankinhalt * 10 - self.zuladung * 50
        self.reichweite = ergebnis - self.zuladung * 50
        print(f'Die Reichweite des LKW {self.marke} mit dem Tankinhalt {self.tankinhalt} L und {self.zuladung} t Zuladung beträgt {self.reichweite} KM')


#auto1 = Fahrzeug('Skoda', 45)
#print(auto1.reichweite_berechnen())

lkw1 = schwererLKW('Mercedes', 150, 12)
lkw1.reichweite_berechnen()