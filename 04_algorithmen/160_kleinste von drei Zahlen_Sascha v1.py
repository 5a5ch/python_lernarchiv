# Kleinste von drei unterschiedlichen Zahlen

from random import randint

a = b = c = 1

while a == b or a == c or b == c:
    a = randint(1,5)
    b = randint(1,5)
    c = randint(1,5)

print(f'Zufallsgenerator: {a}, {b}, {c}')

if a <= b <= c:
    print(f'{a} <= {b} <= {c}')

if a <= c <= b:
    print(f'{a} <= {c} <= {b}')

if b <= a <= c:
    print(f'{b} <= {a} <= {c}')

if b <= c <= a:
    print(f'{b} <= {c} <= {a}')

if c <= a <= b:
    print(f'{c} <= {a} <= {b}')

if c <= b <= a:
    print(f'{c} <= {b} <= {a}')