# Aufgabe 1: Objektinteraktion in Python
# Szenario In der objektorientierten Programmierung (OOP) interagieren Objekte häufig miteinander, um eine gemeinsame
# Funktionalität zu realisieren. In diesem Szenario soll das Zusammenspiel zwischen einem Lichtschalter und einer Lampe
# modelliert werden.
# Gegenstand der Aufgabe Erstellen Sie ein kurzes Sequenzdiagramm mit den beiden Objekten :Lampe und :Schalter. Das SD
# heißt Lampe einschalten
# Schreiben Sie ein Python-Programm, das die Klassen Lampe und Schalter definiert. Der Schalter steuert die Lampe,
# indem er das Lampen-Objekt als Parameter in einer Methode übergeben bekommt.

import time


class Lampe():

    def einschalten(self):
        print('Stromkreis für Lampe geschlossen. Lampe leuchtet.')

    def ausschalten(self):
        print('Stromkreis für Lampe geöffnet. Lampe leuchtet nicht.')


class Schalter():

    def druecken(self,p_schalten):
        print('der Schalter wird gedrückt.')
        p_schalten.einschalten()

    def nochmal_druecken(self, p_schalten):
        print('der Schalter wird nochmal gedrückt.')
        p_schalten.ausschalten()



ledlampe1 = Lampe()
tuerschalter1 = Schalter()


# Lampe an, Lampe wieder aus durch Drücken des Schalters
tuerschalter1.druecken(ledlampe1)
time.sleep(2)
tuerschalter1.nochmal_druecken(ledlampe1)


