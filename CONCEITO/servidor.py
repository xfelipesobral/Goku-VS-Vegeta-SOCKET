from socket import *

'''
# TCP

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

servidor_stat = True
i = 0

s = socket(AF_INET, SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()
print("SERVIDOR INICIADO :D")
conn, addr = s.accept()

while servidor_stat:
    msg = input("DIGITE: ")

    if(msg == "SAIR"):
        servidor_stat = False
    else:
        conn.send(str.encode(msg))
        client_msg = conn.recv(1024)
        print("CLIENTE: "+client_msg.decode())
    
s.close()

'''

#UDP

HOST = "192.168.0.102"
PORT = 12346

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    data, addr = s.recvfrom(1024)

    print(addr,": ", data.decode())

