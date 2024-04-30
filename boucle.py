# -*- coding: utf-8 -*-

#https://fr.wikibooks.org/wiki/Les_ASCII_de_0_%C3%A0_127/La_table_ASCII

#borne sup table ASCII (maj)
supmaj = 90
#borne inf table ASCII (maj)
infmaj = 65

def boucle_alphabet(valeur):
    while valeur > supmaj:
        valeur = valeur - 26
    while valeur < infmaj:
        valeur = valeur + 26
    return valeur