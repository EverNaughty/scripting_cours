import paramiko
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Déclarer l'ip et les credentials pour accéder
ssh.connect('172.16.203.129', username='root', key_filename="C:\\Users\\Arthur\\.ssh\\id_rsa")

# Demande de la valeur à rechercher et des fichiers à utiliser à l'utilisateur
print ("Outil de recherche dans les logs (syslog & auth.log)")
recherche = input("Indique la valeur à rechercher :")
fichiers = input("Indique les fichiers de log à utiliser (séparés par des espaces) :")
print ("La recherche aura lieu dans les fichier suivants :",fichiers)

# Créer la commande à exécuter
commande = "grep -i {} {}".format(recherche, fichiers)

# Note perso :
# Les accolades permettent de déclarer les variables après grâce au .format(1, 2) dans l'ordre
# Cela nous permet de corriger l'erreur d'insertion d'une variable dans le stdin

# Exécuter la commande et récupérer les résultats
stdin, stdout, stderr = ssh.exec_command(commande)

# Formater les résultats
results = stdout.readlines()
# Retour à la ligne à chaque valeur découverte pour une meilleure visibilité
propre = "\n".join(results)

# Afficher les résultats
print(propre)

ssh.close()