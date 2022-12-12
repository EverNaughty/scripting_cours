# Instructions :
# Ecrire un programme qui prend un emoji et qui l'écrit dans le terminal le nombre de fois voulu
# Ce nombre doit être compris entre 3 et maximum 15 fois
# En défaut il le met 5 fois si pas d'argument de l'utilisateur


# Renvoi des instructions d'utilisation en cas d'erreur lors de l'appel du script, génère un manuel
import argparse

# Débit du parser
parser = argparse.ArgumentParser(
                    prog = "Gatling a Emojis V1",
                    description = "Floodeur d'emojis pro",
                                )

# Listing des arguments attendus
parser.add_argument('-e', '--emoji')
# Valeur par défaut si argument non utilisé
parser.add_argument('-n', '--number', default=5)

args = parser.parse_args()

# On stocke les arguments dans des variables
emoji = args.emoji
nombre = args.number
# Transformation de la variable STR en INT
nombre = int(nombre)
# Multiplication
result = emoji*nombre

# Pas d'opération au dessus de 15
if nombre >= 16:
    print ("Invalide")
else:
    print (result)





