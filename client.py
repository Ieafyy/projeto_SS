import socket
from part2 import generate_data
from time import sleep

# ----------------------------------------------------
# REALIZA A COMUNICAÇÃO COM O SERVER
host = '127.0.0.1'
port = 5000

UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (host, port)
print("CLIENTE INICIADO!")
# ----------------------------------------------------

while True:
    data = generate_data()
    UDP.sendto(data.encode('unicode_escape'), server)
    print(data + "ENVIADO COM SUCESSO!")
    sleep(1)
