import random
liste_zufälliger_zahlen = list(range(48,57)) + list(range(65,90)) + list(range(97,122)) + list(range(33,48))
pw = []    # Passwort-Liste
pw_gen_zahlen = []
x = 0      # Index für Liste
anzahl_pw_stellen = 900     # Passwort-Stellen
check_ziff = False
check_grossbuchstabe = False
check_kleinbuchstabe = False
check_sonderzeichen = False
check_laenge = False


for i in range(anzahl_pw_stellen):
    zuf_zahl = random.choice(liste_zufälliger_zahlen)
    pw_gen_zahlen.append(zuf_zahl)
    pw.append(chr(zuf_zahl))
    #x += 1
    if i == 8:
        i = 1
    if len(pw) == 8:
        check_laenge = True
    if len(pw) == 9:
        pw.clear()
        pw_gen_zahlen.clear()
        check_ziff = False
        check_grossbuchstabe = False
        check_kleinbuchstabe = False
        check_sonderzeichen = False
        check_laenge = False
    if zuf_zahl > 47 and zuf_zahl < 58: # Prüfung auf Ziffer
        check_ziff = True
    if zuf_zahl > 64 and zuf_zahl < 91: # Prüfung auf Großbuchstabe
        check_grossbuchstabe = True
    if zuf_zahl > 96 and zuf_zahl < 123: # Prüfung auf Kleinbuchstabe
        check_kleinbuchstabe = True
    if zuf_zahl > 32 and zuf_zahl < 48:   # Prüfung auf Sonderzeichen
        check_sonderzeichen = True
    if check_laenge == True and check_ziff == True and check_grossbuchstabe == True and check_kleinbuchstabe == True and check_sonderzeichen == True:
        break





print(pw_gen_zahlen)
print(f'generiertes Passwort: {pw}')
print(f'Prüfung Ziffer: {check_ziff}')
print(f'Prüfung Großbuchstabe: {check_grossbuchstabe}')
print(f'Prüfung Kleinbuchstabe: {check_kleinbuchstabe}')
print(f'Prüfung Sonderzeichen: {check_sonderzeichen}')
