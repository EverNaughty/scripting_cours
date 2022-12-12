# Ecrire une fonction, on lui donne du texte, elle transforme tout le texte en majuscules si au moins 2 caractères des 4 premiers sont en majuscules, sinon elle retourne la string

def mafonction(a):
    maj_count = 0
    prems = a[:4]
    for word in prems:
        if word.isupper():
            maj_count += 1
    if maj_count >= 2:
        print (a.upper())
    else:
        print (a)     

a = input("Indiquez une chaine de caractère : ")
print = (mafonction(a))