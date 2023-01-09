import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Déclarer l'ip et les credentials pour accéder
ssh.connect('172.16.203.129', username='root', key_filename="C:\\Users\\Arthur\\.ssh\\id_rsa")

# La commande à exécuter sur le serveur et dont on récupère l'output
stdin, stdout, stderr = ssh.exec_command('uptime')
print (stdout.readlines())
ssh.close()