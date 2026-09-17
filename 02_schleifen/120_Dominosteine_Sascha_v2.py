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

# Version 2
# Nachdem in Version 1 jede Reihe einzeln programmiert wurde,
# wird die Aufgabe hier mit verschachtelten Schleifen gelöst.

x = 0
y = 0

for x in range(x, 7):

    print(' ' * 6 * x, end='')

    for y in range(x, 7):
        print(f'{x}|{y}', end='   ')

    print()

    x = x + 1