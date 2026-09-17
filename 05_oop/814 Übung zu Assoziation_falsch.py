# Aufgabe 1: Assoziation „Fahrer und Auto“
# Szenario: Ein Fahrer nutzt ein Auto. Das Auto existiert unabhängig vom Fahrer.
# # Arbeitsauftrag:
#
# Erstellen Sie eine Klasse Auto mit dem Attribut modell.
#
# Erstellen Sie eine Klasse Fahrer mit dem Attribut name und einer Referenz auto (Standardwert None).
#
# Implementieren Sie im Fahrer die Methode einsteigen(auto).
#
# Implementieren Sie im Fahrer die Methode fahren(), die den Modellnamen ausgibt oder meldet, dass kein Auto
# vorhanden ist.

class Auto():
    def __init__(self, p_modell):
        self.modell = p_modell


class Fahrer():
    def __init__(self, p_name):
        self.name = p_name
        self.auto = None

    def einsteigen(self, auto):
        self.auto = auto
        print('du steigst ein')

    def fahren(self):
        
        print(f'Koi gescheits Auto da. Nur n oller {p_auto}!')

Kutsche = Auto('Mazda')
Marc = Fahrer('Marc')


# Marc.einsteigen()
Marc.fahren(Kutsche)