# # Aufgabe 1: Die typenbasierte Rechnungsprüfung
#
# **Szenario:** Ein Abrechnungssystem verarbeitet Rechnungsbeträge je nach Datentyp unterschiedlich. Ganze Eurobeträge
# (**int**) werden direkt als Pauschale gebucht, während exakte Centbeträge (**float**) für die Buchhaltung mit
# Nachkommastellen formatiert werden müssen. Beide Fälle werden über denselben Methodennamen gesteuert.
#
# **Arbeitsauftrag:**
#
# 1. Das Modul mittels `from multipledispatch import dispatch` importieren.
#
# 2. Eine Klasse `RechnungsPruefer` erstellen.
#
# 3. Die Methode `verarbeite_betrag` zweimal mit dem Decorator `@dispatch` definieren:
#
#    * **Variante 1:** Akzeptiert exakt den Typ `int`. Ausgabe auf der Konsole:
#      > "Ganzzahliger Betrag ohne Nachkommastellen verbucht: \[Wert] Euro."
#
#    * **Variante 2:** Akzeptiert exakt den Typ `float`. Ausgabe auf der Konsole:
#      > "Gleitkommazahl-Betrag mit Nachkommastellen verbucht: \[Wert] Euro."
#
# 4. Ein Objekt der Klasse instanziieren, beide Varianten aufrufen (einmal mit der Ganzzahl `250`,
# einmal mit der Gleitkommazahl `99.95`) und die Ausgaben prüfen.

from multipledispatch import dispatch

class RechnungsPruefer:
    @dispatch(int)
    def verarbeite_betrag(self, wert ):
        print(f'Ganzzahliger Betrag ohne Nachkommastellen verbucht: {wert} Euro.')

    @dispatch(float)
    def verarbeite_betrag(self, wert):
        print(f'Gleitkommazahl-Betrag mit Nachkommastellen verbucht: {wert} Euro.')


betrag1 = RechnungsPruefer()

betrag1.verarbeite_betrag(250)
betrag1.verarbeite_betrag(99.95)
