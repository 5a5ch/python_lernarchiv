# Dominosteine

# Gib alle möglichen Dominosteine in der folgenden Form aus.
# Falls jemand das Spiel nicht kennt:
# https://de.wikipedia.org/wiki/Domino

"""
(0|0)(0|1)(0|2)(0|3)(0|4)(0|5)(0|6)
     (1|1)(1|2)(1|3)(1|4)(1|5)(1|6)
          (2|2)(2|3)(2|4)(2|5)(2|6)
               (3|3)(3|4)(3|5)(3|6)
                    (4|4)(4|5)(4|6)
                         (5|5)(5|6)
                              (6|6)
"""

# Version 1
# Erste funktionierende Lösung.
# Jede Reihe wurde einzeln programmiert.

# Dominostein mit Kombination (x|y)

# Reihe 1
x = 0
y = 0

while True:
    if y > 6:
        break

    print(f'{x}|{y}', end='   ')
    y = y + 1

print()

# Reihe 2
x = 1
y = 1

print(' ' * x * 6, end='')

while True:
    if y > 6:
        break

    print(f'{x}|{y}', end='   ')
    y = y + 1

print()

# Reihe 3
x = 2
y = 2

print(' ' * x * 6, end='')

while True:
    if y > 6:
        break

    print(f'{x}|{y}', end='   ')
    y = y + 1

print()

# Reihe 4
x = 3
y = 3

print(' ' * x * 6, end='')

while True:
    if y > 6:
        break

    print(f'{x}|{y}', end='   ')
    y = y + 1

print()

# Reihe 5
x = 4
y = 4

print(' ' * x * 6, end='')

while True:
    if y > 6:
        break

    print(f'{x}|{y}', end='   ')
    y = y + 1

print()

# Reihe 6
x = 5
y = 5

print(' ' * x * 6, end='')

while True:
    if y > 6:
        break

    print(f'{x}|{y}', end='   ')
    y = y + 1

print