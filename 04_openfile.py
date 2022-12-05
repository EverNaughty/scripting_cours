#Ouvrir un fichier avec python
# with open ("text.txt", "a") as f:#as file
#     #append ajoute alors que write remplace
#     f.write("Hello World")

import sys

fichier = input("Indiquer le fichier à éditer :")
contenu = input("Quel texte ajoutez-vous ?")

fichier, contenu = sys.argv[1], sys.argv[2]
with open(fichier, "w") as f:
    f.write(contenu)