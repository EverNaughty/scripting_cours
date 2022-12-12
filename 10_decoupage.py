# Instruction : Découper une phrase à chaque espace

# Import du module REGEX
import re

# Définition de la fonction
def fonction_separateur(a):
    # Découpage en utilisant le séparateur espace
    decoupe = re.split(' ', a)
    return decoupe
    
a = input("Donnez un texte avec des espaces : ")

print (fonction_separateur(a))