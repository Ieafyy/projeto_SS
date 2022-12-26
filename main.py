from time import sleep
import socket
from part1 import read_data

# ----------------------------------------------------
# REALIZA A ABERTURA DO SERVIDOR PARA RECEBER DADOS DO CLIENT
host = '127.0.0.1'
port = 5000

UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (host, port)
UDP.bind(server)
print('OK!')
print('-----------------------')
# ----------------------------------------------------


while True:
    data = str(UDP.recvfrom(1024))
    data = data[3:35]
    read_data(data)
    print(data + ' RECEBIDO COM SUCESSO!')
    #sleep(0.1)
