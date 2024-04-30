# -*- coding: utf-8 -*-

from tkinter import *
from affichage import result

frame = Tk() #créer fenêtre
frame.title("Chiffre de César") #titre fenêtre
frame.geometry("500x200") #dimensionnement fenêtre

#affichage pour entrer du texte
label_texte = Label(frame, text="Entrer du texte : ")
label_texte.pack()

#champ pour entrer du texte
valeurtexte = StringVar()
valeurtexte.set("HELLO WORLD")
texte = Entry(frame, width=50, textvariable=valeurtexte)
texte.pack()

#affichage pour entrer le décalage
label_decalage = Label(frame, text="Entrer le décalage : ")
label_decalage.pack()

#champ pour entrer le décalage
valeurdecalage = StringVar()
valeurdecalage.set("8")
decalage = Entry(frame, width=5, textvariable=valeurdecalage)
decalage.pack()

#boutton circulaire pour l'alphabet en boucle
booleanalphabet = BooleanVar()
booleanalphabet.set(True)
alphabet = Checkbutton(frame, text="Lettres en boucle", variable=booleanalphabet)
alphabet.pack()

#affichage pour choisir la fonction
label_fonction = Label(frame, text="Choisissez la fonction : ")
label_fonction.pack()

#bouttons encodage/décodage
button_encodage = Button(frame, text="Encodage", command=lambda:result(True, texte.get(), booleanalphabet.get(), decalage.get()))
button_encodage.pack()
button_decodage = Button(frame, text="Decodage", command=lambda:result(False, texte.get(), booleanalphabet.get(), decalage.get()))
button_decodage.pack()

frame.mainloop()