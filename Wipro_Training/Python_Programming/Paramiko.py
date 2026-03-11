import paramiko
host = "localhost"
port = 22
username = "Teja angam"
password = "teju"

#create an object and connect to remote machines
client = paramiko.SSHClient()

client.connect(
    hostname = host,
    port = port,
    username = username,
    password = password,
)
stdin, stdout, stderr = client.exec_command("whoami")
print(stdout.read().decode())
client.close()