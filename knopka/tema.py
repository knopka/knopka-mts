import paramiko, base64
#key = paramiko.RSAKey(data=base64.decodestring('AAA...'))
client = paramiko.SSHClient()
#client.get_host_keys().add('ssh.example.com', 'ssh-rsa', key)
client.connect('172.30.32.5', username='kireev', password='4eeter')
stdin, stdout, stderr = client.exec_command('sh run')
for line in stdout:
    print '... ' + line.strip('\n')
client.close()
