# Kleinste von drei unterschiedlichen Zahlen

from random import randint

a = b = c = 1

while a == b or a == c or b == c:
    a = randint(1,5)
    b = randint(1,5)
    c = randint(1,5)

print(f'Zufallsgenerator: {a}, {b}, {c}')

rf = [a,b,c]

rf.sort()

print(rf)