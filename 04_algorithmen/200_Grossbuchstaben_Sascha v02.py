# Großbuchstaben

# Schreibe ein Python-Programm, das sämtliche existierenden Kombinationen
# aus zwei großen Buchstaben auf den Bildschirm schreibt.

def buchstabensuppe(m, n):

    x = m         # zweite Variable für while
    y = n         # zweite Variable für while
    z = m         # Variable für Zeilenwechsel mit neuem 1. Buchstaben

    while m < x + 26 and n < y + 26:

        b1 = chr(n)
        b2 = chr(m)

        print(f'{b1}{b2}', end=' ')

        m += 1

        if m == z + 26:
            n += 1
            m = z
            print()


anfwert1 = int(input('ASCII-Wert für Buchstabe 1 eintippen (Tipp: 65 = A)\n'))
anfwert2 = int(input('ASCII-Wert für Buchstabe 2 eintippen (Tipp: 65 = A)\n'))

buchstabensuppe(anfwert1, anfwert2)

# buchstabensuppe(int(input('ASCII Startwert für Buchstabe 1 und 2 kommagetrennt eingeben\n')))