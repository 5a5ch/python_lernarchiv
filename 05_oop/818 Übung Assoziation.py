# Aufgabe 2: Musikbibliothek
# Ein Nutzer verwaltet eine digitale Musiksammlung. Eine Playlist aggregiert verschiedene Song-Objekte.
# UML-Beschreibung:
# •
# Klasse Song: Attribute: titel (String), interpret (String), dauer (Sekunden).
# •
# Klasse Playlist: Attribute: name (String), songs (Liste). Methoden: song_hinzufuegen(song),
# berechne_gesamtdauer().
# •
# Beziehung: Aggregation (leere Raute an Playlist). Ein Song kann in mehreren Playlists gleichzeitig
# vorhanden sein oder in gar keiner.
# Ihre Aufgabe: Erstellen Sie zunächst das entsprechende Klassendiagramm mit dem Beziehungstyp.
# Setzen Sie dieses Modell in Python um.
# 1.
# Erstellen Sie eine Liste mit 5 unabhängigen Song-Objekten.
# 2.
# Erstellen Sie zwei Playlist-Objekte (z.B. "Favoriten" und "Training").
# 3.
# Fügen Sie denselben Song beiden Playlists hinzu.
# 4.
# Implementieren Sie die Methode berechne_gesamtdauer() so, dass sie die Summe der Sekunden aller
# enthaltenen Songs zurückgibt.

class Song():
    def __init__(self, p_titel, p_interpret, p_dauer):
        self.titel = p_titel
        self.interpret = p_interpret
        self.dauer = p_dauer
        self.eintrag_fuer_pl = f'{self.interpret} - {self.titel}'

class Playlist():
    def __init__(self, p_name):
        self.name = p_name
        self.songs = []
        self.ges_dauer = []

    def hinzufuegen(self, song):
        self.songs.append(song.eintrag_fuer_pl)
        self.ges_dauer.append(song.dauer)

    def gesamtdauer(self):
        print(f'Gesamtlänge der PL "{self.name}": {sum(self.ges_dauer)} Sekunden')



song1 = Song('On A Plain', 'Nirvana', 210)
song2 = Song('In Hiding', 'Pearl Jam', 220)
song3 = Song('Hallelujah', 'Jeff Buckley', 300)
song4 = Song('Banana Pancakes', 'Jack Johnson', 180)
song5 = Song('Playground', 'Bea Miller', 195)

pl1 = Playlist('slow n wow')
pl2 = Playlist('auf die Mütze')

# Song zu PL hinzufügen
pl1.hinzufuegen(song3)
pl1.hinzufuegen(song4)
pl1.hinzufuegen(song5)
pl2.hinzufuegen(song1)
pl2.hinzufuegen(song2)
pl2.hinzufuegen(song5)

# gefüllte PL
print(pl1.songs)
print(pl2.songs)


# Dauer der PL
pl1.gesamtdauer()
pl2.gesamtdauer()


