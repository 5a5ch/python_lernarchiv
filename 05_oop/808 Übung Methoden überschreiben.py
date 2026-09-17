# Hier ist der aus dem Bild ausgelesene Text:
#
# # Aufgabe 1: Mitarbeitersystem und Gehaltsabrechnung
#
# **Szenario:** Ein Unternehmen verwaltet seine Belegschaft über ein Software-System. Es gibt Angestellte mit einem festen
# Grundgehalt und Manager, die zusätzlich einen Bonus erhalten.
#
# ## Arbeitsauftrag:
#
# 1. Eine Basisklasse `Mitarbeiter` erstellen. Der Konstruktor initialisiert die Attribute `name` und `grundgehalt`.
#
# 2. In der Klasse `Mitarbeiter` eine Methode `berechne_gehalt(self)` implementieren. Diese soll den Wert des Attributs `grundgehalt`
# zurückgeben (`return`).
#
# 3. Eine abgeleitete Klasse `Manager` erstellen, die von `Mitarbeiter` erbt. Der Konstruktor nimmt zusätzlich das Attribut `bonus` auf.
#
# 4. Die Methode `berechne_gehalt(self)` in der Klasse `Manager` so überschreiben, dass die Summe aus `grundgehalt` und `bonus`
# zurückgegeben wird.
#
# 5. Ein Objekt der Klasse `Manager` instanziieren (z. B. 4000 Euro Grundgehalt, 1500 Euro Bonus). Die Methode `berechne_gehalt()`
# aufrufen und das Gesamtergebnis auf der Konsole ausgeben.

class Mitarbeiter:
    def __init__(self, p_name, p_grundgehalt):
        self.name = p_name
        self.grundgehalt = p_grundgehalt

    def berechne_gehalt(self):
        return self.grundgehalt

class Manager(Mitarbeiter):
    def __init__(self, p_name, p_grundgehalt, p_bonus):
        super().__init__(p_name, p_grundgehalt)
        self.bonus = p_bonus
        #self.gehalt = self.bonus + self.grundgehalt
    def berechne_gehalt(self):
        self.gehalt = self.bonus + self.grundgehalt
        return self.gehalt



#mitarbeiter1 = Mitarbeiter('Berti', 2500)
#print(mitarbeiter1.berechne_gehalt())

manager1 = Manager('Mike', 4000, 1500)
print(manager1.berechne_gehalt())
