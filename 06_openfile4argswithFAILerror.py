import sys

# On ne demande pas le 4eme argument car on le definira par def
# sauf si l'utilisateur le spécifie lui-même

fichier, contenu, fin = sys.argv[1], sys.argv[2], sys.argv[3]

if len(sys.argv) == 5:
    nbr = sys.argv[4]
else:
    nbr = 1

contenu = contenu + "\n"

with open(fichier, "w") as f:
                    f.write(contenu * int(nbr))
                    f.write(fin)