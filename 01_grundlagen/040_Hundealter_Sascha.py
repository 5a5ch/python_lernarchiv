
# Hundealter

# Hundeliebhaber stellen sich häufig die Frage,
# wie alt ihr Hund wohl wäre, wenn er kein Hund, sondern ein Mensch wäre.
# Landläufig rechnet man Hundejahre in Menschenjahre um,
# indem man das Alter des Hundes mit 7 multipliziert.
# Je nach Hundegröße und Rasse sieht die Umrechnung jedoch etwas komplizierter aus,
# z.B.:
# - Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
# - 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
# - Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

# Schreibe ein Programm, das das Alter eines Hundes erfragt und dann nach obiger
# Methode berechnet, welchem Alter in Menschenjahren das entspricht.

# Wie alt ist der Hund
alter = input('Wie alt ist dein Hund\n')
print(f'Danke. Dein Hund ist {alter} Jahr(e) alt. Umgerechnet in Hundejahre ergibt das:')

# Umwandlung in eine Zahl
alter = int(alter)

if 1 == alter:
    print('Das Hundealter entspricht etwa einem 14-jährigem Menschen')
elif 2 == alter:
    print('Das Hundealter entspricht etwa einem 22-jährigem Menschen')
else:
    print(f'Das Hundealter entspricht etwa einem {(((alter - 2) * 5) + 22)}-jährigen Menschen')
