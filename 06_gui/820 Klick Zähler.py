# Aufgabe 1: Klick-Zähler (Grundlagen)
# Ziel: Erstellung eines Fensters mit einer Schaltflache und einer Textanzeige. Ein Klick auf
# die Schaltfläche erhöht den angezeigten Zählerwert um eins.
#
# Anforderungen
# · Das Fenster trägt den Titel "Klick-Zähler".
#
# · Ein Textfeld zeigt zu Beginn "Klicks: 0".
#
# . Eine Schaltfläche ist mit "Klick mich!" beschriftet.
#
# . Eine Funktion verarbeitet den Klick und aktualisiert die Anzeige.


# GUI mit tkinter

# ist das verbreitetste Modul Python-GUI-Package
# https://tkdocs.com

# Der Stern als Platzhalter (Wildcards) importiert alles von diesem Package
from tkinter import *

# ein Tk-Objekt erzeugen
fenster = Tk()
print(type(fenster))   # <class 'tkinter.Tk'>

fenster.title('Klick-Zähler')
fenster.geometry('340x200')
# Label (Beschriftungen)
# Label() ist der Konstruktor der Klasse Label
x = 0
label_alter = Label(fenster, font=('Arial', 24), width=17, text=f'Klicks {x}')
label_alter.grid(row=0, column=0)



# Funktion für den folgenden Button
# x = 0
def clicked():
    global x
    x = x + 1
    #label_alter = Label(fenster, font=('Arial', 24), width=17, text=f'Klicks {x}')
    #label_alter.grid(row=0, column=0)
    label_alter.configure(text=f'Klicks {x}')




# Button
button = Button(fenster, text='klick mich', command=clicked, font=('Arial', 18))
button.grid(row=1, column=0)



# Muss am Ende stehen, da es die Erzeugung des Fenster startet!!!
fenster.mainloop()
