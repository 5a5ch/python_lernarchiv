# Aufgabe 1: Erstelle eine Klasse 'Auto' mit den Attributen marke und baujahr. Erzeuge zwei Objekte und gib ihre Werte aus.

class Auto():

    # Konstruktor bauen
    def __init__(self, p_baujahr, p_marke, p_preis,p_maxGeschwindigkeit):
        self.baujahr = p_baujahr   # Attribute
        self.marke = p_marke
        self.preis= p_preis
        self.maxGeschwindigkeit = p_maxGeschwindigkeit
        self.geschwindigkeit = 0


    # Methode
    def beschreibung(self):
        return f'Das Auto ist von der Marke {self.marke} und ist im {self.baujahr} gebaut worden. Es kostet aktuell {self.preis} Euro.'
    def beschleunigen(self, wert):
        self.geschwindigkeit = self.geschwindigkeit + wert
    def bremsen(self, wert):
        self.geschwindigkeit = self.geschwindigkeit - wert

# Objekte erzeugen

elektroauto = Auto(2020, 'VW',40000, 162)    # Konstruktoraufruf + Argumente, Daten
hybridauto = Auto(2018, 'Toyota', 32000, 184)


# Ausgabe

# print(f'Preis: {elektroauto.preis}')
#print(elektroauto.beschreibung())

hybridauto.beschleunigen(100)   # durch .beschleunigen wird die Geschwindigkeit überschrieben
print(hybridauto.geschwindigkeit)      # 100

hybridauto.bremsen(20)           # durch .bremsen wird die Geschwindigkeit erneut überschrieben
print(hybridauto.geschwindigkeit)      # 80


