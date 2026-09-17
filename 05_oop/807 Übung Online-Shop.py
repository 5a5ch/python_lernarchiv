# # Aufgabe 3: Das Online-Shop Kundenkonto
#
# **Szenario:** Ein Online-Shop unterscheidet zwischen Standard-Kunden und Premium-Kunden. Alle Kunden besitzen eine eindeutige
# Kundennummer.
#
# ## Arbeitsauftrag:
#
# 1. Eine Basisklasse `Kunde` mit dem Attribut `kundennummer` definieren.
#
# 2. Eine abgeleitete Klasse `PremiumKunde` erstellen, die von `Kunde` erbt.
#
# 3. Der Konstruktor der Klasse `PremiumKunde` soll zusätzlich das Attribut `rabatt` (z. B. als Ganzzahl für Prozentwerte) aufnehmen.
#
# 4. Ein Objekt der Klasse `PremiumKunde` mit einer Kundennummer und einem Rabatt von 15 Prozent instanziieren. Beide Werte
# anschließend zur Überprüfung mittels `print()` ausgeben.

class Kunde:
    def __init__(self, p_kundennr):
        self.kundennr = p_kundennr

class PremiumKunde(Kunde):
    def __init__(self, p_kundennr, p_rabatt):
        self.kundennr = p_kundennr
        #super()__init__(p_kundennr)
        self.rabatt = p_rabatt

premkunde1 = PremiumKunde(999, 15)
print(f'Kundennummer: {premkunde1.kundennr}\nRabatt: {premkunde1.rabatt}%')

