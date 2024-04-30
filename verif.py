# -*- coding: utf-8 -*-

#verifier si les lettres sont en majuscules ou minuscules et comprises dans l'alphabet
def verification (chaine):
    for caractere in chaine:
        if caractere == " ":
           continue
        if caractere >= 'A' and caractere <= 'Z':
            pass
        elif caractere >= 'a' and caractere <= 'z':
            pass
        elif caractere == ' ':
            pass
        else:
            return False
    return True