# String : a chaque espace découpé dans une liste

# Import du module REGEX
import re

# Définition de la fonction
def mafonction(a):
    # Découpage en utilisant le séparateur espace
    decoupe = re.split(' ', a)
    print (decoupe)

a = input("Donnez un texte avec des espaces : ")
(mafonction(a))