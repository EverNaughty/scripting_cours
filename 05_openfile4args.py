import sys

fichier, contenu, fin, nbr = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
contenu = contenu + "\n"
with open(fichier, "w") as f:
    f.write(contenu * int(nbr))
    f.write(fin)
    