#Aufgabe1 Erstelle eine Klasse 'Auto' mit den Attributen marke und baujahr. Erzeuge zwei Objekte und gib ihre Werte aus.
#Aufgabe 2: Erweitere die Klasse 'Auto' um eine Methode 'beschreibung()', die eine Textbeschreibung bzw. die Attribute zurückgibt.
class Auto():
    #Konstruktor ist auch eine Mthode, aber eine bsondere zum Erstellen von Attributen
    def __init__(self,p_baujahr,p_marke): # Parameter: p_baujahr und p_marke
        self.baujahr = p_baujahr #self.baujahr und self.marke sind Attribute oder technisch Speicherorte
        self.marke = p_marke
        self.geschwindigkeit = 0.0
    #Methode
    def beschreibung(self):
        return f'Das Auto ist von der Marke {self.marke} und ist im Jahr {self.baujahr} gebaut worden' #f-string
    def beschleunigen(self,wert):
        self.geschwindigkeit = self.geschwindigkeit + wert
    def bremsen(self,wert):
        pass

#2 Objekte erzeugen
elektroauto = Auto(1955,"Opel") # Konstruktoraufruf !!!: Argumente/Daten: 1955, Opel
hybridauto = Auto(1999,"Mercedes")
#Ausgabe
'''print(elektroauto.baujahr)
print(elektroauto.marke)'''
print(elektroauto.beschreibung())
print(hybridauto.beschreibung())
elektroauto.beschleunigen(10)
print(elektroauto.geschwindigkeit)