# Aufgabe 2: Assoziation „Kunde und Kreditkarte“
# Szenario: Ein Kunde besitzt eine Kreditkarte. Die Karte ist ein eigenständiges Objekt, das dem Kunden
# zugeordnet wird.
# Arbeitsauftrag:
#
#
# Erstellen Sie eine Klasse Kreditkarte mit dem Attribut kartennummer.
#
#
# Erstellen Sie eine Klasse Kunde mit dem Attribut name. Der Kunde erhält seine Kreditkarte direkt bei der
# Initialisierung (init).
#
#
# Implementieren Sie im Kunden die Methode bezahlen(), die die Kartennummer für die Transaktion nutzt.

vergebene_Kreditkarten_Nummern = [0]

class Kredikarte():
    def __init__(self):
        self.kreditkarten_nr = len(vergebene_Kreditkarten_Nummern) + 1000
        vergebene_Kreditkarten_Nummern.append(self.kreditkarten_nr)


class Kunde():
    def __init__(self, p_name):
        self.kunde_name = p_name
        self.zugewiesene_kreditkarte = vergebene_Kreditkarten_Nummern[len(vergebene_Kreditkarten_Nummern)-1]

    def bezahlen(self,p_betrag):
        self.betrag = p_betrag
        print(f'Der Betrag {self.betrag} wird von der Karte mit der Nummer {self.zugewiesene_kreditkarte} abgebucht.')

# Objekte
karte1 = Kredikarte()
kunde1 = Kunde('Saleh')
kunde3 = Kunde('Minh')
karte2 = Kredikarte()
kunde2 = Kunde('Marc')

# Kontrolle
print(kunde1.zugewiesene_kreditkarte)
print(kunde2.zugewiesene_kreditkarte)
print(vergebene_Kreditkarten_Nummern)


# bezahlen mit der Karte
kunde1.bezahlen(100)
kunde2.bezahlen(50)
kunde3.bezahlen(25)