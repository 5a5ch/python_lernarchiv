
# Ulam

# Berühmt ist die (3a + 1)-Folge des amerikanischen Mathematikers Ulam.
# Sie ist durch folgenden Algorithmus definiert:
#
# 1. Beginne mit einem Startwert a.
# 2. Wenn a == 1 ist, stoppe.
# 3. Ist a gerade, setze a = a/2,
#    sonst setze a = 3*a + 1 und fahre mit 2. fort.
#
# Bis heute weiß man nicht,
# ob die Ulam-Folge bei jedem Startwert a zum Stoppen kommt.
#
# Entwickle zu dem Algorithmus eine Funktion
# und teste sie mit verschiedensten Startwerten für a.

a = 2**24   # Startwert a

print(f'Startwert = {a}')

while a != 1:
    x = a%2
    if x == 0:
        a = a / 2
    else:
        a = 3 * a + 1
#    if a == 1:
#        break
    print(a)
