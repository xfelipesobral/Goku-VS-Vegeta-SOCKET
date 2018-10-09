from socket import *

'''
# TCP

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket(AF_INET, SOCK_STREAM)

s.connect((HOST, PORT))

cliente_stat = True

while cliente_stat:
    msg = input("DIGITE: ")

    if(msg == "SAIR"):
        cliente_stat = False
    else:
        s.send(str.encode(msg))
        servidor_msg = s.recv(1024)
        print("SERVIDOR: "+servidor_msg.decode())

s.close()
'''

#UDP

HOST = "192.168.0.102"
PORT = 12346

s = socket(AF_INET, SOCK_DGRAM)

while True:
    s.sendto(str.encode(input("MENSAGEM: ")),(HOST,PORT))
    
s.close()