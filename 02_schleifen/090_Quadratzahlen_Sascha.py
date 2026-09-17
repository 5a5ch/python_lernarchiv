# Quadratzahlen ganzer Zahlen, die kleiner sind als 100
# Anzahl der Ergebnisse ausgeben


zahl = 1
n = 0
while True:
    qz = zahl * zahl
    if qz > 99:
        break
    print(zahl,' ins Quadrat ist ', qz)
    zahl = zahl + 1
    n=n+1

print('Anzahl der Durchläufe: ',n)

