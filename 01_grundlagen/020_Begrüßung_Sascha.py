# Begrüßung

# Es soll eine Begrüßung in Abhängigkeit zur Uhrzeit ausgegeben werden.

# Zwischen 22Uhr und 5Uhr: Gute Nacht
# Vor 11Uhr: Guten Morgen
# Vor 15Uhr: Mahlzeit
# Vor 18Uhr: Guten Nachmittag
# Vor 22Uhr: Guten Abend

# Benutze zum Testen randint(0, 23),
# um eine Zahl von 0 bis 23 zu erzeugen.

from random import randint

zeit = randint(0,23)

print(f'Es ist jetzt {zeit} Uhr.')

if zeit < 5:
    print('Guads Nächdle')
elif zeit < 15:
    print('Mahlzeit!')
elif zeit < 18:
    print('Guten Nachmittag')
elif zeit < 22:
    print('Guadn Abnd!')
else:
    print('Guads Nächdle')