# Urlaubsanspruch

# Betriebsvereinbarung:
# Allen Beschäftigten stehen 26 Tage Urlaub zu.
# Minderjährige Beschäftigte erhalten 30 Tage Urlaub.
# Beschäftigte, die älter als 55 Jahre sind, erhalten 28 Tage Urlaub.
# Beschäftigte mit einer Behinderung ab 50 % erhalten
# zusätzlich 5 weitere Tage Urlaub.
# Beschäftigte mit einer Betriebszugehörigkeit von mehr als 10 Jahren
# erhalten 2 zusätzliche Tage Urlaub.


# -----------------------------
# Lösung 2
# -----------------------------

alter = int(input('Dein Alter, Alter!\n'))   # Eingabe des Alters + integer-Klassifizierung

# Bestimmung des grundsätzlichen Urlaubsanspruchs

if alter < 18:
    urlaub = 30

if 17 < alter < 56:
    urlaub = 26

if alter > 55:
    urlaub = 28


mitBehinderung = input('50% oder mehr Behinderung? j/n\n')   # zusätzlicher Anspruch wegen Behinderung?

if mitBehinderung == 'j':
    urlaub = urlaub + 5


bzug = input('länger als 10 Jahre in diesem Saftladen? j/n\n')   # zusätzlicher Anspruch wegen Zugehörigkeit?

if bzug == 'j':
    urlaub = urlaub + 2


# Ausgabe

print('Alter: ', alter)
print('Jahresurlaub: ', urlaub)