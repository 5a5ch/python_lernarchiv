# Großbuchstaben

# Schreibe ein Python-Programm, das sämtliche existierenden Kombinationen
# aus zwei großen Buchstaben auf den Bildschirm schreibt.

def buchstabensuppe(m, n):

    while m < 91 and n < 91:
        b1 = chr(n)
        b2 = chr(m)

        print(f'{b1}{b2}', end=' ')

        m += 1

        if m == 91:
            n += 1
            m = 65
            print()


anfwert1 = int(input('Wert 65 eintippen\n'))
anfwert2 = int(input('Wert 65 eintippen\n'))

buchstabensuppe(anfwert1, anfwert2)