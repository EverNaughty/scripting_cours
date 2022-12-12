import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.8.134', username='root', key_filename="C:\\Users\\Arthur\\.ssh\\id_rsa")

stdin, stdout, stderr = ssh.exec_command('uptime')
print (stdout.readlines())
ssh.close()