# Urlaubsanspruch
#
# Für die Bestimmung des Urlaubsanspruchs der Beschäftigten einer Firma
# soll ein Programm entwickelt werden.
# Die Grundlage für die Berechnung des Urlaubsanspruchs
# bildet die Betriebsvereinbarung.
# Das Programm soll die Anzahl der Urlaubstage für
# jeweils einen Beschäftigten berechnen.
#
# Betriebsvereinbarung:
# Allen Beschäftigten stehen 26 Tage Urlaub zu.
# Minderjährige Beschäftigte erhalten 30 Tage Urlaub.
# Beschäftigte, die älter als 55 Jahre sind, erhalten 28 Tage Urlaub.
# Beschäftigte mit einer Behinderung ab 50 % erhalten
# zusätzlich 5 weitere Tage Urlaub.
# Beschäftigte mit einer Betriebszugehörigkeit von mehr als 10 Jahren
# erhalten 2 zusätzliche Tage Urlaub.


# -----------------------------
# Lösung 1
# -----------------------------

print('Bitte geben Sie nachfolgend die abgefragten Daten ein und dieses Programm errechnet ihren Jahresurlaub.')

alter = int(input('Bitte geben Sie ihr Alter an.\n'))
behindi = int(input('Haben Sie eine Behinderung von 50% oder höher? ja = 1 oder nein = 0.\n'))
bzug = int(input('Arbeiten Sie schon mehr als 10 Jahre in diesem Betrieb? ja = 1 oder nein = 0.\n'))

# Abfrage für unter 18-Jährige

if alter < 18 and behindi == 1 and bzug == 1:
    print(f'Ihnen stehen insgesamt {30+5+2} Tage Urlaub pro Jahr zu.')

if alter < 18 and behindi == 1 and bzug == 0:
    print(f'Ihnen stehen insgesamt {30+5} Tage Urlaub pro Jahr zu.')

if alter < 18 and behindi == 0 and bzug == 1:
    print(f'Ihnen stehen insgesamt {30+2} Tage Urlaub pro Jahr zu.')

if alter < 18 and behindi == 0 and bzug == 0:
    print(f'Ihnen stehen insgesamt {30} Tage Urlaub pro Jahr zu.')

# Abfrage für 18-55-Jährige

if 17 < alter < 56 and behindi == 1 and bzug == 1:
    print(f'Ihnen stehen insgesamt {26+5+2} Tage Urlaub pro Jahr zu.')

if 17 < alter < 56 and behindi == 1 and bzug == 0:
    print(f'Ihnen stehen insgesamt {26+5} Tage Urlaub pro Jahr zu.')

if 17 < alter < 56 and behindi == 0 and bzug == 1:
    print(f'Ihnen stehen insgesamt {26+2} Tage Urlaub pro Jahr zu.')

if 17 < alter < 56 and behindi == 0 and bzug == 0:
    print(f'Ihnen stehen insgesamt {26} Tage Urlaub pro Jahr zu.')

# Abfrage für ab 56 Jahre

if alter > 55 and behindi == 1 and bzug == 1:
    print(f'Ihnen stehen insgesamt {28+5+2} Tage Urlaub pro Jahr zu.')

if alter > 55 and behindi == 1 and bzug == 0:
    print(f'Ihnen stehen insgesamt {28+5} Tage Urlaub pro Jahr zu.')

if alter > 55 and behindi == 0 and bzug == 1:
    print(f'Ihnen stehen insgesamt {28+2} Tage Urlaub pro Jahr zu.')

if alter > 55 and behindi == 0 and bzug == 0:
    print(f'Ihnen stehen insgesamt {28} Tage Urlaub pro Jahr zu.')


# -----------------------------
# Lösung 2 (angefangen, nicht fertig)
# -----------------------------
#
# Idee:
# Urlaubstage schrittweise berechnen,
# statt alle Kombinationen einzeln abzufragen.
#
# alter2 = input('Dein Alter, Alter!')
# int(alter2)
#
# Hier wurde ein zweiter Lösungsansatz begonnen,
# aber nicht weiter ausgearbeitet.