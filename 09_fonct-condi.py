# Ecrire une fonction, on lui donne du texte, elle transforme tout le texte en majuscules si au moins 2 caractères des 4 premiers sont en majuscules, sinon elle retourne la string

def mafonction(a):
    maj_count = 0
    #Exctraction des 4 premiers caractères
    prems = a[:4]
    #Analyse de type de lettre avec compteur
    for word in prems:
        if word.isupper():
            maj_count += 1
    #Condition sur le nombre de maj
    if maj_count >= 2:
        a = a.upper()
        print (a)
    else:
        print (a)     

a = input("Indiquez une chaine de caractère : ")
print = (mafonction(a))