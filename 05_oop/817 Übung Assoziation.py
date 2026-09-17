# Aufgabe 1: Projektmanagement-System
# Ein Unternehmen verwaltet Projekte. In diesem Szenario besteht ein Projekt aus mehreren Mitarbeitern.
# UML-Beschreibung:
# •
# Klasse Mitarbeiter: Attribute: name (String), rolle (String). Methode: info() zur Textausgabe.
# •
# Klasse Projekt: Attribute: titel (String), mitarbeiter_liste (Liste von Mitarbeiter-Objekten). Methoden: hinzufuegen(mitarbeiter), anzeigen_team().
# •
# Beziehung: Aggregation zwischen Projekt (Ganzes) und Mitarbeiter (Teile). Die Mitarbeiter werden außerhalb des Projekts erstellt und existieren weiter,
# auch wenn ein Projekt abgeschlossen (gelöscht) wird.
# Ihre Aufgabe: Erstellen Sie zunächst das entsprechende Klassendiagramm mit dem Beziehungstyp.
# Implementieren Sie beide Klassen in Python. Erstellen Sie drei Mitarbeiter-Objekte und ordnen Sie zwei davon einem Projekt-Objekt zu. Demonstrieren Sie,
# dass die Mitarbeiter-Objekte nach dem Löschen des Projekts (del projekt_name) weiterhin verfügbar sind.


class Mitarbeiter():
    def __init__(self, p_name, p_rolle):
        self.name = p_name
        self.rolle = p_rolle

    def info(self):
        print(f'Mitarbeitername: {self.name}, Rolle: {self.rolle}')

class Projekt():
    def __init__(self, p_titel):
        self.titel = p_titel
        self.mitarbeiter_liste = []

    def hinzufuegen(self, p_mitarbeiter):
        self.mitarbeiter_liste.append(p_mitarbeiter)
        #print(f'{p_mitarbeiter.name} wurde dem Projekt {self.titel} hinzugefügt')

    def anzeigen_team(self):
        print(self.mitarbeiter_liste)

def loeschen(p_projekt):
    del p_projekt
    print('Projekt wird gelöscht')


# Mitarbeiter-Objekte
Sascha = Mitarbeiter('Sascha', 'Kaffeekoch')
Marc = Mitarbeiter('Marc', 'Programmierer')
Minh = Mitarbeiter('Minh', 'Penetrator')

Sascha.info()
Marc.info()
Minh.info()

# Projekt-Objekte
Prj1 = Projekt('LF08')
Prj2 = Projekt('AP1')

# MA zu Prj hinzufügen
Prj1.hinzufuegen(Marc.name)
Prj1.hinzufuegen(Minh.name)
Prj2.hinzufuegen(Sascha.name)
Prj2.hinzufuegen(Marc.name)
#print(Prj1.mitarbeiter_liste)
#print(Prj2.mitarbeiter_liste)
Prj1.anzeigen_team()
Prj2.anzeigen_team()

# Projekt1 löschen und zeigen, dass die MA noch vorhanden sind
#del Prj1
loeschen(Prj1)
Sascha.info()
Marc.info()
Minh.info()