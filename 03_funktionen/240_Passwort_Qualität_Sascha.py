# Passwort-Qualität

# Schreibe eine Funktion, die die Qualität von Passwörtern nach
# einem einfachen Punktesystem bewertet.
#
# Regeln:
# – Passwort mit 7 oder weniger Zeichen: immer 0 Punkte
# – Ab 8 Zeichen: 1 Punkt.
# – Enthält sowohl Groß- als auch Kleinbuchstaben: +1 Punkt.
# – Enthält MEHR als sechs unterschiedliche Zeichen: +1 Punkt.
# – Enthält zumindest eine Ziffer: +1 Punkt.
# – Enthält zumindest ein Sonderzeichen: +1 Punkt.


# print(liste1[0])
# pw = 'abc123'
# pw_liste = list(pw)
# print(pw_liste)
# länge = len(pw_liste)
# print(länge)

def q_check(pw):

    c = 0      # counter
    punkte = 0

    pw_liste = list(pw)
    pw_länge = len(pw_liste)

    if pw_länge >= 8:        # Passwort mit mindestens 8 Zeichen
        punkte += 1

    for _ in range(pw_länge):     # Enthält Kleinbuchstaben

        if pw_liste[c].islower():
            pw_kleinbuchstabe = pw_liste[c].islower()
            print(pw_kleinbuchstabe)
            break

        else:
            pw_kleinbuchstabe = False

        c += 1

    c = 0

    for _ in range(pw_länge):     # Enthält Großbuchstaben

        if pw_liste[c].isupper():
            pw_grossbuchstabe = pw_liste[c].isupper()
            print(pw_grossbuchstabe)
            break

        else:
            pw_grossbuchstabe = False

        c += 1

    if pw_kleinbuchstabe == True and pw_grossbuchstabe == True:
        punkte += 1

    pw_dopplungen = list(set(pw_liste))   # Mehr als sechs unterschiedliche Zeichen

    if len(pw_dopplungen) > 6:
        punkte += 1

    c = 0

    for _ in range(pw_länge):    # Enthält Ziffer

        if pw_liste[c].isdigit():
            pw_ziffer = pw_liste[c].isdigit()
            print(pw_ziffer)
            punkte += 1
            break

        else:
            pw_ziffer = False

        c += 1

    c = 0

    for _ in range(pw_länge):    # Enthält Sonderzeichen

        if pw_liste[c].isalnum() == False:
            pw_sonder = pw_liste[c].isalnum()
            print(pw_sonder)
            punkte += 1
            break

        else:
            pw_sonder = True

        c += 1

    # weniger als oder gleich 7 Zeichen = immer 0 Punkte

    if pw_länge <= 7:
        punkte = 0

    return punkte


print(f"Punkte für Qualität des Passworts: {q_check('aaAcd453sdwta')}")