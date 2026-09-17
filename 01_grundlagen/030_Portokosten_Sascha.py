
# Portokosten

"""
Die Portokosten (Versandkosten) sind wie folgt festgelegt:
Unter 39.99 € Bestellwert kosten 3.99 € Porto
40 - 69.99 € Bestellwert kosten 2.99 € Porto
70 - 99.99 € Bestellwert kosten 1.99 € Porto
ab 100 € ist portofrei

Es soll eine Zufallszahl (bestellwert)
von 1.00 - 130.00 erzeugt werden (z.B. 40.47, 123.78)

Dann soll ermittelt werden,
wie hoch die entsprechenden Portokosten sind.
Am Ende sollen der Bestellwert, die Portokosten
und der Gesamtbetrag ausgegeben werden.
"""

#Zufallszahl
import random
zahl = round(random.uniform(1.00,130.00),2)
print(f'Deine Bestellung hat den Warenwert von {zahl} €.')

# Porto-Bedingung

if zahl < 39.99:
    porto1 = 3.99
    print(f'Das Porto beträgt {porto1} €. Die Summe ist {zahl + porto1} €.')
elif 39.99 <= zahl < 69.99:
    porto2 = 2.99
    print(f'Das Porto beträgt {porto2} €. Die Summe ist {zahl + porto2} €.')
elif 69.99 <= zahl < 99.99:
    porto3 = 1.99
    print(f'Das Porto beträgt {porto3} €. Die Summe ist {zahl + porto3} €.')
else:
    print(f'Die Bestellung ist versandkostenfrei. Die Summe ist {zahl} €.')
