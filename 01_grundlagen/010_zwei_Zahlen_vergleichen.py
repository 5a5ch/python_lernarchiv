# zwei Zahlen genau vergleichen

# schreibe ein Programm, das teste und ausgibt
# welche der beiden Zahlen ist größer oder sind sie gleich groß

from random import randint

zahl1 = randint(1, 10)
zahl2 = randint(1, 10)
print('zufällige Zahl 1:',zahl1)
print('zufällige Zahl 2:',zahl2)
print()
if zahl1 > zahl2:
    print('Zahl 1 ist größer als Zahl 2.')
elif zahl2 > zahl1:
    print('Zahl 2 ist größer als Zahl 1.')
else:
    print('Die beiden Zahlen sind gleichgroß.')

