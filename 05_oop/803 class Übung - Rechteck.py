# Aufgabe 4: Erstelle eine Klasse 'Rechteck' mit breite und höhe sowie einer Methode flaeche(), die die Fläche berechnet.

class Rechteck:
    def __init__(self, p_breite, p_hoehe):
        self.breite = p_breite
        self.hoehe = p_hoehe

    def flaeche(self):
        self.flaeche = self.breite * self.hoehe
        print(f'Der Flächeninhalt für das Rechteck mit der Breite {self.breite} cm und Höhe {self.hoehe} cm beträgt {self.flaeche} qcm.')

    def umfang(self):
        self.umfang = 2 * self.breite + 2 * self.hoehe
        print(f'Der Umfang für das Rechteck mit der Breite {self.breite} cm und Höhe {self.hoehe} cm beträgt {self.umfang} cm.')

    def diagonal(self):
        self.diagonal = (self.breite * self.breite + self.hoehe * self.hoehe) ** (1/2)
        print(f'Die Diagonale ist {self.diagonal} cm.')


'''zahl = 25                                                Wurzel ziehen in Pyton
wurzel = zahl ** 0.5 oder zahl ** (1/2)
print(wurzel)  # 5.0
'''


rechteck1 = Rechteck(10, 10)
rechteck1.flaeche()
rechteck1.umfang()
rechteck1.diagonal()