
# Web-Code

# Für ein Buchprojekt wird ein Web-Code benötigt.
# Mit diesem Web-Code können Artikel direkt online abgefragt werden.
# Der Code soll aus acht Zeichen bestehen.
# Vorkommen dürfen Ziffern und Kleinbuchstaben.
# Um Verwechslungen zu vermeiden,
# kommen die Ziffer Eins (1) und der Kleinbuchstabe "ell" (l) nicht vor.
# Ebenso kommt die Null (0) nicht vor.
# Dass das große "Oh" (Systemadministration) nicht vorkommen kann, ist klar,
# denn die Vorgabe erlaubt nur Kleinbuchstaben.
#
# Schreibe ein Programm, das fünf zufällige Web-Codes erzeugt.


verfüg_zeichen = []


for i in range(50,58):
    verfüg_zeichen.append(chr(i))

for i in range(97,123):
    if i != 108:
        verfüg_zeichen.append(chr(i))

# print(len(verfüg_zeichen))

from random import randint

webcode = []
for _ in range(5):
    for i in range(8):
        x = randint(0,30)
        #print(x)
        y = verfüg_zeichen[x]
        webcode.append(y)
    webcode_str = ''.join(webcode)
    print(webcode_str)
    webcode.clear()
