# Definition d'une fonction
# On défini la fonction :
def mafonction(a, b):
    return a*b

# On demande les valeurs :
txt = (input("Donner une chaine de caractère :"))
nbr = (input("Donner un nombre :"))
# On déclare bien un entier int :
nbr = int(nbr)

# On passe les valeurs dans la fonction
print (mafonction(txt, nbr))
