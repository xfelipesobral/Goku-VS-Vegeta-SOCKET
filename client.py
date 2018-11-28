import socket

def enviar(udp, data, destino):
    udp.sendto(data.encode(), destino)

def initClient():
    HOST = 'localhost' 
    PORT = 5000     

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)

    enviar(udp, "CONECTEI$jogo", dest)

    while True:
        data, ip = udp.recvfrom(1024)

        data = data.decode()
        data = data.split('$')
        chave = data[0]

        if(chave == "CONECTEI"):
            if(data[1] != "conectou"):
                udp.close()
            else:
                print("10")

        if(chave == "BROADCAST_PLAYER"):
            print(data[1])