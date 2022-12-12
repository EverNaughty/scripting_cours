#Fonction retournant le nombre de maj et de min d'un texte

#Définition de la fonction
def compteur(texte):

    UP = 0
    LOW = 0

    for i in texte:
        if i in updico:
            UP += 1

    for i in texte:
        if i in lowdico:
            LOW += 1

    print ("Majuscules :",UP,"et minuscules :",LOW)

#Inventaire de lettres
updico = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowdico = "abcdefghijklmnopqrstuvwxyz"

#Récupération du string str
texte = input("Give me a text !")

print (compteur(texte))

