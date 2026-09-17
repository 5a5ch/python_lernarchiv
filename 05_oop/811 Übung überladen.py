# # Aufgabe 2: Der ID- und Code-Scanner
#
# **Szenario:** Ein Einlasssystem an einem Werkstor scannt Berechtigungen. Mitarbeiter besitzen eine rein
# numerische Personalnummer (`int`). Externe Dienstleister besitzen einen alphanumerischen Zugangscode,
# der als Text (`str`) vorliegt. Das System verarbeitet beide ID-Typen über dieselbe Methode.
#
# **Arbeitsauftrag:**
#
# 1. Eine Klasse `ZugangsScanner` erstellen.
#
# 2. Die Methode `pruefe_identitaet` zweimal mittels `@dispatch` überladen:
#
#    * **Variante 1:** Akzeptiert ein Argument vom Typ `int`. Ausgabe:
#      > "Mitarbeiter-ID erkannt. Status: Interner Zugriff gewährt für ID \[Wert]."
#
#    * **Variante 2:** Akzeptiert ein Argument vom Typ `str`. Ausgabe:
#      > "Dienstleister-Code erkannt. Status: Temporärer Zugriff gewährt für Code \[Wert]."
#
# 3. Ein Objekt der Klasse instanziieren und die Methode mit passenden Testdaten aufrufen (z. B.
# einmal mit der Zahl `1024` und einmal mit dem Text `"EXT-9988"`).

from multipledispatch import dispatch

class Zugangsscanner:
    @dispatch(int)
    def pruefe_id(self,wert):
        print(f'Mitarbeiter-ID erkannt. Status: Interner Zugriff gewährt für ID {wert}.')

    @dispatch(str)
    def pruefe_id(self,wert):
        print(f'Dienstleister-Code erkannt. Status: Temporärer Zugriff gewährt für Code {wert}.')

id_int_1 = Zugangsscanner()
id_ext_1 = Zugangsscanner()

id_int_1.pruefe_id(18115884135)
id_ext_1.pruefe_id('ABcd')
