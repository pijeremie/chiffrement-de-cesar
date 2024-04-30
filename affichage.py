# -*- coding: utf-8 -*-

from tkinter import Message
from cryptage import chiffrage
from verif import verification
from numeric_converter import convertnumeric
 
#resultat cryptage ou décryptage
def result(mode, chaine, alphabet, decalage_entier):
    try:
        decalage_entier = convertnumeric(decalage_entier)
    except ValueError:
        decalage_entier = 0
        print("Numéro de décalage incorrect !")

    if verification(chaine) == True:
        decalage_entier = int(decalage_entier)       
        if mode == True:
            print(chiffrage(chaine, +decalage_entier, alphabet)) #chiffrement
        else:
            print(chiffrage(chaine, -decalage_entier, alphabet)) #dechiffrement
    else:
        print("Veuillez n'entrer que des lettres en majuscules ou minuscules et des espaces !")