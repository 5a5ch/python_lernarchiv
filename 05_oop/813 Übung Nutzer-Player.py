# Aufgabe 2: Objektinteraktion in Python
# Szenario: Ein Nutzer bedient einen Musik-Player. Der Player startet ein Lied und stoppt es nach einer Weile wieder
# Gegenstand der Aufgabe
# Erstellen Sie ein kurzes Sequenzdiagramm mit den beiden Objekten :Nutzer und :MusikPlayer. Das SD heißt Musik hören.
# Die Nachrichten heißen song_abspielen() und musik_stoppen().
# Setzen Sie das Diagramm in Python-Code um.

import time

class Nutzer():

    def musikhören(self, player):
        print('Nutzer drückt auf Play')
        time.sleep(0.5)

        player.song_abspielen()

        time.sleep(3)

        print('Nutzer drückt auf Stop')
        time.sleep(0.5)

        player.musik_stoppen()


class MusikPlayer():

    def song_abspielen(self):
        print('Musik wird gespielt.')

    def musik_stoppen(self):
        print('Musik ist gestoppt.')


Marc = Nutzer()
iPod = MusikPlayer()

Marc.musikhören(iPod)