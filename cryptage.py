# -*- coding: utf-8 -*-

import string
from boucle import boucle_alphabet

#crypter ou decrypter en fonction du décalage 
def chiffrage(chaine, decalage_entier, alphabet):
    liste = []
    stringconvertie = ""
    for caractere in chaine:
        if caractere == " ":
            liste.append(" ")
        else:
            caractere = caractere.upper()
            if alphabet == True:
                liste.append(chr(boucle_alphabet(ord(caractere) + decalage_entier)))
            else:
                liste.append(chr(ord(caractere) + decalage_entier))
    return stringconvertie.join(liste) 