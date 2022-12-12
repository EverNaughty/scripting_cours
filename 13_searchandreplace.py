import argparse
import shutil
import os

parser = argparse.ArgumentParser(
                    prog = "Research & Destr..Replace",
                    description = "Remplacement d'occurences",
                    )

parser.add_argument('file')
parser.add_argument('-rech', '--rechercher')
parser.add_argument('-remp', '--remplacer')

args = parser.parse_args()

fin = open(args.file, "r")

# Fichier de sortie temporairement différent
fout = open("text2.txt", "wt")

# Pour chaque ligne faire un remplacement
for line in fin:
	fout.write(line.replace(args.rechercher, (args.remplacer)))

# Fermeture
fin.close()
fout.close()

# Remplace l'ancien fichier par le nouveau
shutil.copyfile('text2.txt', 'text.txt')
# Supprime le fichier temporaire créé
os.remove("text2.txt")