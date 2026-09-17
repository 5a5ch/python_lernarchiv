
# Größter gemeinsamer Teiler

# Schreibe eine rekursive Funktion, die den größten
# gemeinsamen Teiler (den ggt) von zwei Zahlen berechnet.
# Dabei handelt es sich um die größte Zahl,
# durch den beide Zahlen ohne Rest dividiert werden können.
#
# Die Funktion soll den euklidischen Algorithmus implementieren.
# Dieser besagt:
# – Dividiere die größere Zahl durch die kleinere.
# – Wenn der Rest 0 ist, ist die kleinere Zahl der gesuchte ggt.
# – Sonst: wiederhole den Vorgang, wobei als neuer Ausgangspunkt die
#          vormals kleinere Zahl und der Rest dienen.
#
# Beispiel:
# – 80 / 65 = 1, Rest 15. Weiter mit 65 und 15
# – 65 / 15 = 4, Rest 5. Weiter mit 15 und 5
# – 15 / 5 = 3, Rest 0. Der ggt ist daher 5


def teiler(x, y):
    for _ in range(y):
        z1 = x % y
        #z2 = x // y
        if z1 == 0:
            return y
        else:
            x = y
            y = z1

print(f'der ggT ist {teiler(100, 50)}')